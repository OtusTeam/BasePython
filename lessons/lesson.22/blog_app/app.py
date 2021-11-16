from typing import Optional

from fastapi import FastAPI, Body, Depends, Query
from starlette.status import HTTP_201_CREATED
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from blog_app import crud
from blog_app.dependencies import get_user_by_token
from blog_app.models import User
from blog_app.models.database import session_dependency
from blog_app.models.db_async import get_session
from blog_app.schemas import UserIn, UserOut, CalcInput

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello world!!!"}


@app.get("/{user_id}/friends/")
def get_friends(user_id: int):
    return {
        "id": user_id,
        "friends": [
            {
                "id": 2345,
                "bd": None,
                "close_friend": False,
            }
        ],
    }


@app.post("/items/")
def create_item(data: dict = Body(...)):
    """
    # Header
    ## Header 2
    ### Header 3

    - item
    - item
    - item

    some `code` and _some italic_

    Creates new item
    """
    return {
        "item": data,
    }


@app.get("/add/")
def add_two_numbers(a: int, b: int):
    return {"sum": a + b}


@app.get("/sub/")
def sub_two_numbers(
    # query string dependency
    q: Optional[str] = Query(None),
    # query string dependency too!
    calc_input: CalcInput = Depends(),
):
    return {
        "q": q,
        "sub": calc_input.a - calc_input.b,
    }

#
#


@app.get("/users/me/", response_model=UserOut)
def get_me(user: User = Depends(get_user_by_token)):
    return user


@app.post("/users/", response_model=UserOut, status_code=HTTP_201_CREATED)
async def create_user(
    user_in: UserIn,
    session: AsyncSession = Depends(get_session),
):
    user = await crud.create_user(session, user_in)
    return user


@app.post("/users/create-many/", response_model=list[UserOut])
async def create_many_users(
    users_count: int,
    session: AsyncSession = Depends(get_session),
):
    users = await crud.create_users(session, count=users_count)
    return users


@app.get("/users/", response_model=list[UserOut])
async def get_users(session: AsyncSession = Depends(get_session)):
    users = await crud.list_users(session)
    return list(users)


@app.get("/users/sync/", response_model=list[UserOut])
def get_users_sync(session: Session = Depends(session_dependency)):
    users = crud.list_users_sync(session)
    return users
