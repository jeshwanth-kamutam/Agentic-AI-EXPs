"""
Multi-agent text-to-SQL pipeline built with CrewAI.

Agents:
  1. Retriever    -- pulls the relevant schema chunks + few-shot examples
                     for the user's question (TF-IDF retrieval, no LLM call).
  2. SQL Generator -- LLM writes a SQL query grounded in the retrieved context.
  3. Validator     -- guardrail + EXPLAIN dry-run; on failure, feeds the error
                     back to the SQL Generator for up to MAX_RETRIES corrective
                     attempts before giving up.
  4. Explainer     -- LLM turns the executed result rows into a plain-English
                     answer.

The Retriever and Validator steps are deterministic Python (no LLM needed),
which keeps them fast, cheap, and testable. Only SQL generation and the
final explanation go through the LLM, via CrewAI Agents/Tasks.

Model/provider is configured through environment variables (see .env.example)
and read by litellm under the hood -- swap MODEL to point at Groq, OpenAI,
Anthropic, etc.
"""
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from crewai import Agent, Task, Crew, Process
from retrieval.schema_retriever import TfidfRetriever
from tools.sql_tools import validate_sql, execute_sql

MODEL = os.environ.get("LLM_MODEL", "groq/llama-3.3-70b-versatile")
MAX_RETRIES = 2


def _format_schema_context(chunks) -> str:
    return "\n\n".join(c.text for c in chunks)


def _format_examples(examples) -> str:
    return "\n".join(f"Q: {e.question}\nSQL: {e.sql}" for e in examples)


def build_agents():
    sql_generator = Agent(
        role="SQL Generator",
        goal="Write a single correct, read-only SQLite SELECT query that answers the user's question.",
        backstory=(
            "An expert SQLite analyst. You only ever write SELECT statements. "
            "You strictly use the table and column names given in the schema "
            "context -- never invent names. You return ONLY the raw SQL, no "
            "markdown fences, no commentary."
        ),
        llm=MODEL,
        verbose=False,
    )

    explainer = Agent(
        role="Result Explainer",
        goal="Turn raw SQL result rows into a short, clear natural language answer.",
        backstory=(
            "A data analyst who explains query results to non-technical "
            "stakeholders in 1-3 concise sentences, referencing actual "
            "numbers/values from the results."
        ),
        llm=MODEL,
        verbose=False,
    )
    return sql_generator, explainer


def _generate_sql(sql_generator: Agent, question: str, schema_ctx: str,
                   examples_ctx: str, prior_error: str = None, prior_sql: str = None) -> str:
    correction_note = ""
    if prior_error:
        correction_note = (
            f"\n\nYour previous attempt failed validation.\n"
            f"Previous SQL: {prior_sql}\n"
            f"Error: {prior_error}\n"
            f"Fix the query and try again."
        )

    task = Task(
        description=(
            f"Database schema context (only these tables/columns exist):\n{schema_ctx}\n\n"
            f"Example question/SQL pairs for style reference:\n{examples_ctx}\n\n"
            f"User question: {question}"
            f"{correction_note}\n\n"
            "Return ONLY the SQL query, nothing else."
        ),
        expected_output="A single raw SQLite SELECT statement, no markdown, no explanation.",
        agent=sql_generator,
    )
    crew = Crew(agents=[sql_generator], tasks=[task], process=Process.sequential, verbose=False)
    result = crew.kickoff()
    return str(result).strip()


def _explain_results(explainer: Agent, question: str, columns, rows) -> str:
    preview = ", ".join(
        "(" + ", ".join(f"{c}={v}" for c, v in zip(columns, r)) + ")" for r in rows[:20]
    )
    task = Task(
        description=(
            f"User question: {question}\n"
            f"Result columns: {columns}\n"
            f"Result rows (up to 20 shown): {preview}\n\n"
            "Write a concise natural-language answer using the actual values above."
        ),
        expected_output="1-3 sentence plain-English answer.",
        agent=explainer,
    )
    crew = Crew(agents=[explainer], tasks=[task], process=Process.sequential, verbose=False)
    result = crew.kickoff()
    return str(result).strip()


def run_pipeline(question: str, db_path: str, retriever: TfidfRetriever = None) -> dict:
    """
    Runs the full Retriever -> Generator -> Validator(+retry) -> Executor ->
    Explainer pipeline. Returns a dict with every intermediate artifact so
    the UI can show its work.
    """
    retriever = retriever or TfidfRetriever(db_path)
    sql_generator, explainer = build_agents()

    # 1. Retrieve
    chunks = retriever.retrieve_schema(question, k=3)
    examples = retriever.retrieve_examples(question, k=2)
    schema_ctx = _format_schema_context(chunks)
    examples_ctx = _format_examples(examples)

    trace = {
        "question": question,
        "retrieved_tables": [c.table for c in chunks],
        "attempts": [],
        "final_sql": None,
        "columns": None,
        "rows": None,
        "answer": None,
        "error": None,
    }

    # 2 & 3. Generate + Validate, with self-correction loop
    sql = None
    error = None
    for attempt in range(MAX_RETRIES + 1):
        sql = _generate_sql(
            sql_generator, question, schema_ctx, examples_ctx,
            prior_error=error, prior_sql=sql,
        )
        validation = validate_sql(db_path, sql)
        trace["attempts"].append({"sql": sql, "valid": validation.ok, "error": validation.error})
        if validation.ok:
            error = None
            break
        error = validation.error
    else:
        pass

    if error:
        trace["error"] = f"Failed to produce a valid query after {MAX_RETRIES + 1} attempts: {error}"
        return trace

    # 4. Execute
    exec_result = execute_sql(db_path, sql)
    if not exec_result.ok:
        trace["error"] = f"Execution failed: {exec_result.error}"
        return trace

    trace["final_sql"] = sql
    trace["columns"] = exec_result.columns
    trace["rows"] = exec_result.rows

    # 5. Explain
    trace["answer"] = _explain_results(explainer, question, exec_result.columns, exec_result.rows)
    return trace


if __name__ == "__main__":
    import json
    result = run_pipeline(
        "What is the total revenue from delivered orders?",
        db_path="db/demo.db",
    )
    print(json.dumps(result, indent=2, default=str))
