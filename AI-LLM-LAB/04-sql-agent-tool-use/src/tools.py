import sqlite3

class SQLTools:
    def __init__(self, db_path="data/store.db"):
        self.db_path = db_path

    def list_tables(self) -> str:
        """Returns a list of tables in the database."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [row[0] for row in cursor.fetchall()]
        conn.close()
        return f"Tables: {', '.join(tables)}"

    def get_schema(self, table_name: str) -> str:
        """Returns the schema for a specific table."""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute(f"SELECT sql FROM sqlite_master WHERE type='table' AND name='{table_name}';")
            schema = cursor.fetchone()
            conn.close()
            return schema[0] if schema else f"Table {table_name} not found."
        except Exception as e:
            return f"Error: {e}"

    def execute_sql(self, sql: str) -> str:
        """Executes a SQL query and returns the results."""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            conn.close()
            return f"Results: {results}"
        except Exception as e:
            return f"Error executing SQL: {e}"
