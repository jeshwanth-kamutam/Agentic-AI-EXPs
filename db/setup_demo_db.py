"""
Creates a small demo SQLite database (demo.db) with a simple e-commerce
schema: customers, products, orders, order_items.

Run: python db/setup_demo_db.py
"""
import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "demo.db")

SCHEMA_SQL = """
DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    name        TEXT NOT NULL,
    email       TEXT NOT NULL,
    country     TEXT NOT NULL,
    signup_date TEXT NOT NULL
);

CREATE TABLE products (
    product_id  INTEGER PRIMARY KEY,
    name        TEXT NOT NULL,
    category    TEXT NOT NULL,
    price       REAL NOT NULL
);

CREATE TABLE orders (
    order_id    INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    order_date  TEXT NOT NULL,
    status      TEXT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE order_items (
    order_item_id INTEGER PRIMARY KEY,
    order_id      INTEGER NOT NULL,
    product_id    INTEGER NOT NULL,
    quantity      INTEGER NOT NULL,
    unit_price    REAL NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
"""

CUSTOMERS = [
    (1, "Ananya Rao", "ananya@example.com", "India", "2023-01-15"),
    (2, "John Smith", "john@example.com", "USA", "2023-02-20"),
    (3, "Wei Zhang", "wei@example.com", "China", "2023-03-05"),
    (4, "Priya Nair", "priya@example.com", "India", "2023-04-11"),
    (5, "Carlos Diaz", "carlos@example.com", "Mexico", "2023-05-01"),
]

PRODUCTS = [
    (1, "Wireless Mouse", "Electronics", 799.0),
    (2, "Mechanical Keyboard", "Electronics", 3499.0),
    (3, "Yoga Mat", "Fitness", 999.0),
    (4, "Water Bottle", "Fitness", 349.0),
    (5, "Novel: The Silent Path", "Books", 449.0),
]

ORDERS = [
    (1, 1, "2024-06-01", "delivered"),
    (2, 2, "2024-06-03", "delivered"),
    (3, 1, "2024-06-10", "shipped"),
    (4, 3, "2024-06-12", "delivered"),
    (5, 4, "2024-06-15", "cancelled"),
    (6, 5, "2024-06-18", "delivered"),
    (7, 4, "2024-06-20", "shipped"),
]

ORDER_ITEMS = [
    (1, 1, 1, 2, 799.0),
    (2, 1, 3, 1, 999.0),
    (3, 2, 2, 1, 3499.0),
    (4, 3, 4, 3, 349.0),
    (5, 4, 5, 2, 449.0),
    (6, 5, 1, 1, 799.0),
    (7, 6, 2, 1, 3499.0),
    (8, 6, 5, 1, 449.0),
    (9, 7, 3, 1, 999.0),
]


def main():
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.executescript(SCHEMA_SQL)
    cur.executemany("INSERT INTO customers VALUES (?,?,?,?,?)", CUSTOMERS)
    cur.executemany("INSERT INTO products VALUES (?,?,?,?)", PRODUCTS)
    cur.executemany("INSERT INTO orders VALUES (?,?,?,?)", ORDERS)
    cur.executemany("INSERT INTO order_items VALUES (?,?,?,?,?)", ORDER_ITEMS)
    conn.commit()
    conn.close()
    print(f"Demo database created at {DB_PATH}")


if __name__ == "__main__":
    main()
