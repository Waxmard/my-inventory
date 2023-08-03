from db.session import init_db, insert_new_item
from db.read import query_all_items

conn = init_db()
insert_new_item(conn, 'clorox wipes', 10, 'Cleaning wipes')
insert_new_item(conn, 'grout cleaner', 5, 'For cleaning grout')

for item in query_all_items(conn):
    print(item)

conn.close()
