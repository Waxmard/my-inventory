def insert_new_item(conn, name, quantity, description):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items WHERE name = ?", (name,))
    existing_item = cursor.fetchone()

    if existing_item is None:
        sql = "INSERT INTO items (name, quantity, description) VALUES (?, ?, ?)"
        cursor.execute(sql, (name, quantity, description))
        conn.commit()
    else:
        raise ValueError(f"Item with name '{name}' already exists in the database.")
