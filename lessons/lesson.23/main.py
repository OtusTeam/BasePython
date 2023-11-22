from typing import Annotated

import uvicorn
from fastapi import FastAPI, Query, Path

from views import items_router, calc_router
from views.api import router as api_router

app = FastAPI()
app.include_router(items_router)
app.include_router(calc_router)
app.include_router(api_router)


@app.get("/")
def hello_index():
    return {"message": "Hello World!"}


@app.get("/hello/")
def hello_user(name: Annotated[str, Query(min_length=3)]):
    return {"message": f"Hello {name}!"}


@app.get("/hello/{name}/")
def hello_user_path(name: str):
    return {"message": f"Hello {name}!!!"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
