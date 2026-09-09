from src.tools import SQLTools
import time

class ReActSQLAgent:
    """Mock implementation of a ReAct Agent."""
    def __init__(self):
        self.tools = SQLTools()

    def run(self, question: str):
        print(f"\n[Agent Started] Goal: {question}")
        
        # Step 1: List tables
        print("[Agent Action] Calling tool: list_tables()")
        time.sleep(0.5)
        tables = self.tools.list_tables()
        print(f"[Tool Result] {tables}")
        
        # Step 2: Get schema
        print("[Agent Action] Calling tool: get_schema(table_name='products')")
        time.sleep(0.5)
        schema = self.tools.get_schema('products')
        print(f"[Tool Result] {schema}")
        
        # Step 3: Execute SQL
        sql = ""
        if "most expensive" in question.lower():
            sql = "SELECT name, price FROM products ORDER BY price DESC LIMIT 1;"
        elif "in stock" in question.lower():
            sql = "SELECT name, stock FROM products WHERE stock > 0;"
        else:
            sql = "SELECT * FROM products LIMIT 1;"
            
        print(f"[Agent Action] Calling tool: execute_sql(sql='{sql}')")
        time.sleep(0.5)
        results = self.tools.execute_sql(sql)
        print(f"[Tool Result] {results}")
        
        # Step 4: Final Answer
        print("[Agent Action] Formulating final answer...")
        time.sleep(0.5)
        
        if "Laptop" in results:
            final_answer = "The most expensive product is the Laptop at $999.99."
        else:
            final_answer = f"Based on the query, the results are: {results}"
            
        print(f"\n[Final Answer] {final_answer}")
        return final_answer
