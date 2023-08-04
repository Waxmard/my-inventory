import os
import sqlite3

from proj.settings import DB_NAME


def _create_connection():
    db_path = '.db/' + DB_NAME
    if not os.path.exists('.db'):
        os.makedirs('.db')
    conn = sqlite3.connect(db_path)
    return conn


def _create_table(conn):
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        description TEXT
    )
    """)
    conn.commit()


def get_conn():
    conn = _create_connection()
    _create_table(conn)
    return conn


def insert_new_item(conn, name, quantity, description):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items WHERE name = ?", (name,))
    existing_item = cursor.fetchone()
    if existing_item is None:
        sql = "INSERT INTO items (name, quantity, description) VALUES (?, ?, ?)"
        cursor.execute(sql, (name, quantity, description))
        conn.commit()
    else:
        print(f"Item with name '{name}' already exists in the database.")
