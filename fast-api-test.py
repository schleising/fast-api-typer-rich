from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Thing(BaseModel):
    age: int
    height: float

    class Config:
        schema_extra = {
            'example': {
                'age': 42,
                'height': 165.78,
            }
        }

class Item(BaseModel):
    name: str
    price: float
    thing: Thing
    is_offer: Union[bool, None] = None

    class Config:
        schema_extra = {
            'example': {
                'name': 'John',
                'price': 77.54,
                'thing': Thing.Config.schema_extra['example'],
                'is_offer': False,
            }
        }


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item) -> Item:
    print(item)
    return item
