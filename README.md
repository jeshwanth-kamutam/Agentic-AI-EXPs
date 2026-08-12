# Text-to-SQL Multi-Agent Workflow

A retrieval-grounded, self-correcting pipeline that turns natural language
questions into SQL, executes them, and explains the results — built as a
4-agent CrewAI pipeline with a Streamlit chat UI.

## Architecture

```
User question
     |
     v
[1] Retriever            TF-IDF similarity search over schema chunks +
    (no LLM)              a few-shot NL->SQL example bank. Returns only
                           the relevant tables/columns instead of the
                           full schema.
     |
     v
[2] SQL Generator (LLM)  Writes a SELECT query using the retrieved
                           context + few-shot examples.
     |
     v
[3] Validator             Blocks non-SELECT / DML / DDL statements, then
    (no LLM)              dry-runs via EXPLAIN. On failure, the error is
                           fed back to [2] for a corrective retry
                           (up to 2 retries).
     |
     v
[4] Executor (no LLM)     Runs the validated query against SQLite.
     |
     v
[5] Explainer (LLM)       Converts result rows into a 1-3 sentence
                           natural-language answer.
     |
     v
Streamlit chat UI (shows the answer + retrieved tables + every SQL
attempt + the result table, in an expandable "pipeline details" panel)
```

Retrieval and validation are deliberately plain Python (no LLM call) —
they're cheap, deterministic, fast, and don't need to hallucinate table
names. Only SQL generation and the final explanation use the LLM.

## Project structure

```
text2sql/
  app.py                     Streamlit chat UI
  db/
    setup_demo_db.py         Creates demo.db (customers/products/orders/order_items)
  retrieval/
    schema_retriever.py      Schema introspection + TF-IDF retrieval + few-shot bank
  tools/
    sql_tools.py             Guardrails (read-only enforcement) + validate/execute
  agents/
    crew.py                  CrewAI agents (SQL Generator, Explainer) + pipeline orchestration
  requirements.txt
  .env.example
```

## Setup

```bash
cd text2sql
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Build the demo database
python db/setup_demo_db.py

# Configure your LLM provider
cp .env.example .env
# edit .env and add your GROQ_API_KEY (or OPENAI_API_KEY / ANTHROPIC_API_KEY)

streamlit run app.py
```

## Try it

- "What is the total revenue from delivered orders?"
- "Which customers are from India?"
- "Top 3 products by quantity sold"
- "Which customers have never placed an order?"

## Swapping in your own database

1. Replace `db/demo.db` with your own SQLite file (or point `DB_PATH` in
   `app.py` at it), or extend `retrieval/schema_retriever.py`'s
   `build_schema_chunks()` to introspect Postgres/MySQL via SQLAlchemy
   instead of `sqlite3` — the rest of the pipeline is DB-agnostic as long
   as `tools/sql_tools.py` executes against the same connection type.
2. Seed `FEW_SHOT_BANK` in `schema_retriever.py` with a handful of real
   question/SQL pairs from your domain — this is the single highest-leverage
   change for accuracy.
3. For larger schemas (20+ tables), swap `TfidfRetriever` for an embedding
   + vector-store retriever (e.g. `sentence-transformers` + ChromaDB) — both
   should expose the same `retrieve_schema()` / `retrieve_examples()`
   interface so `agents/crew.py` doesn't need to change.

## Safety guardrails

- Only `SELECT` statements are ever generated or executed.
- `tools/sql_tools.py` hard-blocks `DROP/DELETE/UPDATE/INSERT/ALTER/
  TRUNCATE/CREATE/...` regardless of how the LLM frames the query.
- Every query is dry-run via `EXPLAIN` before execution; invalid SQL never
  touches the actual data.
- Result rows are capped (`row_limit=200`) to avoid dumping huge tables
  into a single LLM explanation call.

## Notes

- Retrieval and validation were tested directly in this environment (no
  LLM key required) and work correctly, including the self-correction
  path: an invalid query (wrong column name) is caught by `validate_sql`
  and its error message is exactly what gets fed back to the SQL
  Generator agent on retry.
- The SQL Generator / Explainer agents require a live LLM key to run
  (Groq/OpenAI/Anthropic) — add yours to `.env` before starting Streamlit.
