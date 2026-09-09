import sqlite3
import os

def setup_database(db_path="data/enterprise.db"):
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        department TEXT,
        salary REAL
    )
    ''')

    cursor.execute("DELETE FROM employees")

    cursor.executemany("INSERT INTO employees (id, name, department, salary) VALUES (?, ?, ?, ?)", [
        (1, 'Alice', 'Engineering', 120000),
        (2, 'Bob', 'HR', 85000),
        (3, 'Charlie', 'Engineering', 115000)
    ])

    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()
