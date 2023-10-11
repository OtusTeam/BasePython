from typing import Annotated

from fastapi import FastAPI, Query, Path

from views import items_router, calc_router

app = FastAPI()
app.include_router(items_router)
app.include_router(calc_router)


@app.get("/")
def hello_index():
    return {"message": "Hello World!"}


# def hello_user(name: str = Query(min_length=3)):
@app.get("/hello/")
def hello_user(name: Annotated[str, Query(min_length=3)]):
    return {"message": f"Hello {name}!"}


@app.get("/hello/{name}/")
# def hello_user_path(name: str = Path(min_length=3)):
def hello_user_path(name: str):
    return {"message": f"Hello {name}!!!"}
