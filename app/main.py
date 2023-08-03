from db.session import init_db
from db.read import query_all_items
from routers import inventory
from fastapi import FastApi


app = FastApi()
app.include_router(inventory.router, prefix="/inventory")

conn = init_db(db_name='inventory.db')

for item in query_all_items(conn):
    print(item)

conn.close()
