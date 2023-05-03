
from typing import TypedDict, Union, List
from fastapi import FastAPI
from fastapi.responses import FileResponse

class Todo(TypedDict):
    id:str
    text:str

listTodo:List[Todo] = [
    {
        'id':'1',
        'text':'hacer la comida'
    },
    {
        'id':'2',
        'text':'hacer la tarea'
    }
]
app = FastAPI()

# --------------------------------------------------------
@app.get("/")
async def read_root():
    return FileResponse("index.html")

# ------------------------------------------------------

@app.get("/items")
async def read_root():
    return listTodo

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    item = None
    bolean = False
    for valor in listTodo:
        if(int(valor['id'])==item_id):
            item=valor
            bolean=True
            break
    if(bolean is False):
       return {'error':'not found item'}
    return item


@app.post("/items")
async def read_root():
    return {"Here we use": "post"}

@app.patch("/items/{item_id}")
async def read_root(item_id:int):
    return {"Here we use": "update item"}

@app.delete("/items/{item_id}")
async def read_root(item_id:int):
    return {"Here we use": "delete item"}