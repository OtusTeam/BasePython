"""
API - application programming interface
"""
from datetime import datetime

from fastapi import FastAPI

from pydantic import constr

from items_views import router as items_router
from users.views import router as users_router

app = FastAPI()
app.include_router(items_router)
app.include_router(users_router)


@app.get("/")
def root():
    return {"message": "Hello World!!"}


@app.get("/hello")
def hello(name: constr(min_length=3) = "OTUS"):
    return {"message": name, "now": datetime.now()}


@app.get("/add")
def add_values(a: int, b: int):
    return {
        "a": a,
        "b": b,
        "sum": a + b,
    }
