from fastapi import FastAPI

from src.routers import inventory

app = FastAPI()
app.include_router(inventory.router, prefix="/inventory")
