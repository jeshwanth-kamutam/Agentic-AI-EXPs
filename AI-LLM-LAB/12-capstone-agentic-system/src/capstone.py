import sqlite3
import time

class RAGAgent:
    def __init__(self):
        self.knowledge = "Company policy: Engineering bonuses are 10% of salary. HR bonuses are 5%."
    def answer(self, query):
        print("[RAG Agent] Searching vector DB for policy...")
        time.sleep(0.5)
        return self.knowledge

class SQLAgent:
    def __init__(self, db_path="data/enterprise.db"):
        self.db_path = db_path
    def get_salary(self, name):
        print(f"[SQL Agent] Querying DB for {name}'s salary...")
        time.sleep(0.5)
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT department, salary FROM employees WHERE name=?", (name,))
        res = cursor.fetchone()
        conn.close()
        return res

class MasterAgent:
    def __init__(self):
        self.rag = RAGAgent()
        self.sql = SQLAgent()

    def process(self, query: str) -> str:
        print(f"\n=== Master Agent Received Query: '{query}' ===")
        print("[Master Agent] Decomposing query...")
        
        # Routing logic
        if "bonus" in query.lower() and "alice" in query.lower():
            # Need SQL for Salary, RAG for Policy
            print("[Master Agent] Routing to SQL Agent for employee details...")
            emp_data = self.sql.get_salary("Alice")
            
            print("[Master Agent] Routing to RAG Agent for bonus policy...")
            policy = self.rag.answer("bonus policy")
            
            print("[Master Agent] Synthesizing final answer...")
            time.sleep(0.5)
            dept, salary = emp_data
            bonus = salary * 0.10 if dept == "Engineering" else salary * 0.05
            
            return f"Alice is in {dept} with a salary of ${salary}. According to policy, her bonus is ${bonus}."
            
        return "I can only calculate Alice's bonus in this mock."
