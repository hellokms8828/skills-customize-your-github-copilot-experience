from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

# TODO: Define your Pydantic models here
# Example: Create a model for your main resource (e.g., Book, Task, Product)
# class Item(BaseModel):
#     id: int
#     name: str
#     description: Optional[str] = None
#     price: float


# TODO: Create an in-memory data store
# Example: items_db = []


# TODO: Implement GET endpoint to retrieve all items
# @app.get("/items")
# async def get_all_items():
#     pass


# TODO: Implement GET endpoint to retrieve a specific item by ID
# @app.get("/items/{item_id}")
# async def get_item(item_id: int):
#     pass


# TODO: Implement POST endpoint to create a new item
# @app.post("/items", status_code=status.HTTP_201_CREATED)
# async def create_item(item: Item):
#     pass


# TODO: Implement PUT endpoint to update an item
# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     pass


# TODO: Implement DELETE endpoint to remove an item
# @app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
# async def delete_item(item_id: int):
#     pass


# Test endpoint to verify the server is running
@app.get("/")
async def root():
    return {"message": "FastAPI REST API - Ready for implementation"}
