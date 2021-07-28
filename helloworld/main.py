"""Hello world API
    - ref: https://fastapi.tiangolo.com/ja/#_5
"""

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_root():
    return {"Hello": "World"}


@app.get('/items/{item_id}')
def read_item(item_id: int, q: str = None):
    return {"item id": item_id, "query": q}
