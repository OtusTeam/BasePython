from typing import Optional, List

from fastapi import FastAPI, exceptions, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from blog_app import crud
from blog_app.dependencies import get_user_by_token
from blog_app.schemas import UserIn, UserOut
from core.models import User
from core.models.db import get_session
from core.models.db_sync import get_sync_session

app = FastAPI()


@app.get("/", summary="Get a hello world json")
def hello(
    name: str = "World",
):
    """
    Hello world view
    1. processes `request`
    1. returns greeting
    """
    return {"Hello": name}


#

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


#

@app.post("/users", response_model=UserOut, tags=["Users"])
async def create_user(
    user_in: UserIn,
    db_session: AsyncSession = Depends(get_session),
):
    user = await crud.create_user(user_in, db_session)
    return user


@app.post("/users/create-many", response_model=List[UserOut], tags=["Users"])
async def create_many_users(
    users_to_create: int,
    db_session: AsyncSession = Depends(get_session),
):
    users = await crud.create_many_users(users_to_create, db_session)
    return users


@app.get("/users", response_model=List[UserOut], tags=["Users"])
async def get_users(
    db_session: AsyncSession = Depends(get_session),
):
    user = await crud.get_users(db_session)
    return list(user)


@app.get("/users/sync", response_model=List[UserOut], tags=["Users"])
def get_users_sync(
    db_session=Depends(get_sync_session),
):
    users = crud.get_users_sync(db_session)
    return users


@app.get("/users/me", response_model=UserOut, tags=["Users"])
async def get_me(user: User = Depends(get_user_by_token)):
    return user


@app.get("/users/{user_id}", response_model=UserOut, tags=["Users"])
async def get_user(
    user_id: int,
    db_session: AsyncSession = Depends(get_session),
):
    user = await crud.get_user(user_id, db_session)
    if user:
        return user

    raise exceptions.HTTPException(
        404,
        {"message": f"No user with id #{user_id}", "value": user_id},
    )
