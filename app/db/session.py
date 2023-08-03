import os
import sqlite3


def _create_connection(db_name='inventory.db'):
    db_path = '.db/' + db_name
    if not os.path.exists('.db'):
        os.makedirs('.db')
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect(db_path)
    return conn


def _create_table(conn):
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        description TEXT,
        photo BLOB
    )
    """)
    conn.commit()


def init_db():
    conn = _create_connection()
    _create_table(conn)
    return conn


def insert_new_item(conn, name, quantity, description):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items WHERE name = ?", (name,))
    existing_item = cursor.fetchone()
    if existing_item is None:
        cursor.execute("INSERT INTO items (name, quantity, description) VALUES (?, ?, ?)", (name, quantity, description))
        conn.commit()
    else:
        print(f"Item with name '{name}' already exists in the database.")
