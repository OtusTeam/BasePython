from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def index():
    return {"message": "Hello World"}


@app.get("/name/")
async def name_func():
    return {"message": "Hello, Bob"}


@app.post("/item/add")
async def item_func(item_id: int):
    return {"message": item_id + 3000}


@app.get("/item/{item_id}")
async def item_func(item_id: int, q: str = None):
    return {"message": item_id + 1000, 'q': q}


