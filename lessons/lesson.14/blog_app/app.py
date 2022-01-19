from typing import Optional

from fastapi import FastAPI, Body, HTTPException, status, Depends, Query

from blog_app import crud
from blog_app.dependencies import get_user_by_auth_token
from blog_app.schemas import UserIn, UserOut, User, CalcInput

app = FastAPI()


@app.get("/")
def read_root(
    q: Optional[str] = Query(None),
):
    return {"message": "Hello World!!!", "q": q}


@app.get("/hello")
def hello_view(name: str):
    return {"message": f"Hello {name}"}


@app.get("/items/{item_id}", tags=["Items"])
def get_item_by_id(item_id: int):
    return {"id": item_id, "name": "somename"}


@app.post("/items", tags=["Items"])
def create_item(data: dict = Body(...)):
    return {
        "data": data,
    }


@app.get("/add", tags=["Calc"])
def add_values(a: int, b: int):
    return {"sum": a + b}


@app.get("/sub", tags=["Calc"])
def subtract_values(calc_input: CalcInput = Depends()):
    return {
        "data": calc_input.dict(),
        "result": calc_input.a - calc_input.b,
    }


@app.get("/users", response_model=list[UserOut], tags=["Users"])
def list_users():
    return crud.list_users()


@app.post("/users", response_model=UserOut, tags=["Users"])
def create_user(user_in: UserIn):
    user = crud.create_user(user_in)
    return user


@app.get("/users/me", response_model=UserOut, tags=["Users"])
def get_auth_user(user: User = Depends(get_user_by_auth_token)):
    return user


@app.get("/users/{user_id}", response_model=UserOut, tags=["Users"])
def get_user_by_id(user_id: int):
    user = crud.get_user_by_id(user_id)
    if user:
        return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"user #{user_id} not found",
    )
