import sqlite3
import os

def setup_database(db_path="data/university.db"):
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create tables
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS departments (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        department_id INTEGER,
        marks INTEGER,
        FOREIGN KEY(department_id) REFERENCES departments(id)
    )
    ''')

    # Insert sample data
    cursor.execute("DELETE FROM departments")
    cursor.execute("DELETE FROM students")

    cursor.executemany("INSERT INTO departments (id, name) VALUES (?, ?)", [
        (1, 'Computer Science'),
        (2, 'Electrical Engineering'),
        (3, 'Mechanical Engineering')
    ])

    cursor.executemany("INSERT INTO students (id, name, department_id, marks) VALUES (?, ?, ?, ?)", [
        (1, 'Alice Smith', 1, 95),
        (2, 'Bob Johnson', 1, 88),
        (3, 'Charlie Brown', 2, 75),
        (4, 'Diana Prince', 3, 92),
        (5, 'Evan Wright', 1, 85),
        (6, 'Fiona Gallagher', 2, 90)
    ])

    conn.commit()
    conn.close()
    print(f"Database created and seeded at {db_path}")

if __name__ == "__main__":
    setup_database()
