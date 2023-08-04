from proj.models.item import Item


def query_all_items(conn) -> list[Item]:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items")
    columns = [description[0] for description in cursor.description]
    rows = cursor.fetchall()
    return [Item(**dict(zip(columns, row))) for row in rows]
