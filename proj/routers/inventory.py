from fastapi import APIRouter, HTTPException

from proj.db.create import insert_new_item
from proj.db.read import query_all_items
from proj.db.session import get_conn
from proj.models.item import Item

router = APIRouter()


@router.post("/items")
def create_item(item: Item):
    conn = get_conn()
    try:
        insert_new_item(conn, item.name, item.quantity, item.description)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    conn.close()
    return {"message": "Item successfully added"}


@router.get("/items")
def get_items():
    conn = get_conn()
    items = query_all_items(conn)
    conn.close()
    return items
