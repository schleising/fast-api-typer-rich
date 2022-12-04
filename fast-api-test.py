from typing import Union

from fastapi import FastAPI, APIRouter, HTTPException, status, Header, Depends
from pydantic import BaseModel

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


class ResponseItem(BaseModel):
    name: str
    price: float
    thing: Thing

    class Config:
        schema_extra = {
            'example': {
                'name': 'John',
                'price': 77.54,
                'thing': Thing.Config.schema_extra['example'],
            }
        }

class Item(ResponseItem):
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

items = {
    1: Item(name='Item 1', price=25.98, thing=Thing(age=65, height=28.76), is_offer=True),
    2: Item(name='Item 2', price=98.12, thing=Thing(age=12, height=33.43), is_offer=False),
    3: Item(name='Item 3', price=100.78, thing=Thing(age=23, height=12.44), is_offer=False),
    4: Item(name='Item 4', price=87.54, thing=Thing(age=45, height=34.87), is_offer=True),
    5: Item(name='Item 5', price=23.11, thing=Thing(age=68, height=34.12), is_offer=False),
    6: Item(name='Item 6', price=11.33, thing=Thing(age=54, height=113.98), is_offer=True),
    7: Item(name='Item 7', price=879.65, thing=Thing(age=43, height=13.09), is_offer=False),
}


def printThing(user_agent: str = Header()):
    print(f'User Agent: {user_agent}')
    yield
    print('Request Complete')

app = FastAPI()

itemRouter = APIRouter(
    prefix='/items',
    dependencies=[Depends(printThing)]
)

@itemRouter.get("/", response_model=dict[int, ResponseItem])
def read_items():
    return items

@itemRouter.get("/{item_id}", response_model=ResponseItem | Thing | str)
def read_item(item_id: int, q: str | None = None):
    if item_id in items:
        item = items[item_id]
        if q is not None:
            if q in item.dict():
                return f'{q.title()}: {item.dict()[q]}'
            else:
                raise HTTPException(status_code=status.HTTP_418_IM_A_TEAPOT, detail='What are you doing !!?')    
        else:
            return items[item_id]
    else:
        raise HTTPException(status_code=status.HTTP_418_IM_A_TEAPOT, detail='What are you doing !!?')    

@itemRouter.put("/{item_id}", response_model=ResponseItem)
def update_item(item_id: int, item: Item):
    print(item)
    if item_id == 4:
        raise HTTPException(status_code=status.HTTP_418_IM_A_TEAPOT, detail='What are you doing !!?')
    return item

app.include_router(itemRouter)

@app.get("/")
def read_root():
    return {"Hello": "World"}


