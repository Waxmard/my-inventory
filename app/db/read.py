def query_all_items(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items")
    return cursor.fetchall()
