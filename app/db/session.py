import os
import sqlite3


def create_connection(db_name='inventory.db'):
    db_path = '.db/' + db_name

    if not os.path.exists('.db'):
        os.makedirs('.db')
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect(db_path)
    return conn


def create_table(conn):
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


def insert_item(conn, name, quantity, description):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO items (name, quantity, description) VALUES (?, ?, ?)", (name, quantity, description))
    conn.commit()


def close_connection(conn):
    conn.close()
