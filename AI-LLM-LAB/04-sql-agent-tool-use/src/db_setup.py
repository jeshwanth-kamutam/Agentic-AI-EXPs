import sqlite3
import os

def setup_database(db_path="data/store.db"):
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        price REAL,
        stock INTEGER
    )
    ''')

    cursor.execute("DELETE FROM products")

    cursor.executemany("INSERT INTO products (id, name, price, stock) VALUES (?, ?, ?, ?)", [
        (1, 'Laptop', 999.99, 10),
        (2, 'Smartphone', 499.99, 50),
        (3, 'Headphones', 79.99, 100),
        (4, 'Keyboard', 49.99, 30)
    ])

    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()
