from db.create import insert_new_item
from fastapi import ApiRouter, HTTPException
from models.item import Item


router = ApiRouter()


@app.post("/items/")
def create_item(item: Item):
    conn = create_connection()

    try:
        insert_new_item(conn, item.name, item.quantity, item.description)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    conn.close()
    return {"message": "Item successfully added"}
