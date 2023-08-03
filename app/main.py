from db.session import create_connection, create_table, insert_item, close_connection
from db.read import query_all_items

conn = create_connection()
create_table(conn)
insert_item(conn, 'clorox wipes', 10, 'Cleaning wipes')
insert_item(conn, 'grout cleaner', 5, 'For cleaning grout')

for item in query_all_items(conn):
    print(item)

close_connection(conn)
