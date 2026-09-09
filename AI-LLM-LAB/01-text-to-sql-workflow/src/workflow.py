import os
import sqlite3
from typing import Dict, Any
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# A mock LLM function for demonstration without API keys
def mock_llm_call(prompt: str) -> str:
    prompt_lower = prompt.lower()
    if "top 5 students" in prompt_lower:
        return "SELECT name, marks FROM students ORDER BY marks DESC LIMIT 5;"
    elif "how many students" in prompt_lower:
        return "SELECT d.name, COUNT(s.id) FROM departments d LEFT JOIN students s ON d.id = s.department_id GROUP BY d.id;"
    elif "average mark" in prompt_lower or "average score" in prompt_lower:
        return "SELECT AVG(marks) FROM students;"
    elif "answer:" in prompt_lower:
        if "Alice Smith" in prompt_lower:
            return "The top students by marks are Alice Smith (95), Diana Prince (92), Fiona Gallagher (90), Bob Johnson (88), and Evan Wright (85)."
        if "Computer Science" in prompt_lower:
            return "There are 3 students in Computer Science, 2 in Electrical Engineering, and 1 in Mechanical Engineering."
        return "Based on the database results, here is the information you requested."
    return "SELECT * FROM students LIMIT 1;"

class TextToSQLWorkflow:
    def __init__(self, db_path: str = "data/university.db", use_mock: bool = True):
        self.db_path = db_path
        self.use_mock = use_mock
        if not self.use_mock:
            self.llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    
    def get_schema(self) -> str:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT sql FROM sqlite_master WHERE type='table';")
        schemas = cursor.fetchall()
        conn.close()
        return "\n".join([schema[0] for schema in schemas if schema[0]])

    def generate_sql(self, question: str, schema: str) -> str:
        if self.use_mock:
            prompt = f"Given the following database schema:\n{schema}\n\nWrite a SQL query to answer this question: '{question}'\nOutput ONLY the SQL query."
            return mock_llm_call(prompt)
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a SQLite expert. Given the database schema, write a SQL query that answers the user's question. Output ONLY the raw SQL query without any markdown formatting or explanation."),
            ("user", "Schema:\n{schema}\n\nQuestion: {question}")
        ])
        
        chain = prompt | self.llm | StrOutputParser()
        sql = chain.invoke({"schema": schema, "question": question})
        # Clean up in case the LLM returned markdown blocks
        return sql.replace("```sql", "").replace("```", "").strip()

    def execute_sql(self, sql: str) -> Any:
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            conn.close()
            return results
        except Exception as e:
            return f"Error executing SQL: {e}"

    def generate_natural_language_answer(self, question: str, sql: str, results: Any) -> str:
        if self.use_mock:
            prompt = f"Question: {question}\nSQL Query: {sql}\nDatabase Results: {results}\n\nAnswer: Provide a natural language answer based on the results."
            return mock_llm_call(prompt)
            
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a helpful assistant. Synthesize a natural language answer to the user's question based on the provided SQL query and database results."),
            ("user", "Question: {question}\nSQL Query: {sql}\nDatabase Results: {results}")
        ])
        
        chain = prompt | self.llm | StrOutputParser()
        return chain.invoke({"question": question, "sql": sql, "results": str(results)})

    def run(self, question: str) -> Dict[str, Any]:
        print(f"\n--- Processing Question: '{question}' ---")
        
        print("1. Retrieving Schema...")
        schema = self.get_schema()
        
        print("2. Generating SQL...")
        sql = self.generate_sql(question, schema)
        print(f"   Generated SQL: {sql}")
        
        print("3. Executing SQL...")
        results = self.execute_sql(sql)
        print(f"   Query Results: {results}")
        
        print("4. Generating Natural Language Answer...")
        final_answer = self.generate_natural_language_answer(question, sql, results)
        
        return {
            "question": question,
            "sql": sql,
            "results": results,
            "final_answer": final_answer
        }
