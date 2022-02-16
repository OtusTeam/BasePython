from fastapi import FastAPI, HTTPException, status, Depends

from sqlalchemy.orm import Session as SessionType
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from .models.database import session_dependency
from .models.db_async import get_session
from .schemas import UserIn, UserSchemaOut

app = FastAPI()


@app.get("/sync/users", response_model=list[UserSchemaOut], tags=["Users"])
def list_users(session: SessionType = Depends(session_dependency)):
    return crud.list_users(session)


@app.post("/sync/users", response_model=UserSchemaOut, tags=["Users"])
def create_user(
    user_in: UserIn,
    session: SessionType = Depends(session_dependency),
):
    user = crud.create_user(session, user_in)
    return user


@app.get("/users", response_model=list[UserSchemaOut], tags=["Users"])
async def list_users_async(async_session: AsyncSession = Depends(get_session)):
    return await crud.list_users_async(async_session)


@app.post("/users/create-many", response_model=list[UserSchemaOut], tags=["Users"])
async def create_many_users(
    users_count: int,
    async_session: AsyncSession = Depends(get_session),
):
    users = await crud.create_many_users(async_session, users_count)
    return users


@app.get("/users/{user_id}", response_model=UserSchemaOut, tags=["Users"])
async def get_user_by_id(
    user_id: int,
    async_session: AsyncSession = Depends(get_session),
):
    user = await crud.get_user_by_id(async_session, user_id)
    if user:
        return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"user #{user_id} not found",
    )
