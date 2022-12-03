# FastAPI / Pydantic Testing

Testing FastAPI with Pydantic

`fast-api-test.py` defines a class `Item`, a GET route for `/` and GET and PUT routes for `/items/{item_id}`

Using Pydantic the json is automatically serialised to / from the `Item` type

FastAPI also provides auto generated API documentation, try outh the PUT `/items/{item_id}` route to see this in action

## To run
```bash
pip install -r requirements.txt
uvicorn fast-api-test:app --reload
```
Then point the browser at [localhost:8000](http://localhost:8000/)

To view the documentation go to [localhost:8000/docs](http://localhost:8000/docs)
