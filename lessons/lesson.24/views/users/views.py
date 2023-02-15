import asyncio

from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import conint

from models import User
from . import crud
from .dependencies import user_by_token, session_dependency
from schemas.user import UserIn, UserOut

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("", response_model=list[UserOut])
async def get_users(
    session: AsyncSession = Depends(session_dependency),
) -> list[User]:
    return await crud.get_users(session)


@router.post(
    "",
    response_model=UserOut,
    status_code=status.HTTP_201_CREATED,
)
async def create_user(
    user_in: UserIn,
    session: AsyncSession = Depends(session_dependency),
) -> User:
    return await crud.create_user(session, user_in)


@router.get("/me", response_model=UserOut)
def get_me(user: User = Depends(user_by_token)) -> User:
    return user


@router.post(
    "/create-many",
    response_model=list[UserOut],
    status_code=status.HTTP_201_CREATED,
)
async def create_many_users(
    count: conint(ge=1, le=1000),
    session: AsyncSession = Depends(session_dependency),
):
    return await crud.create_many_users(session, count=count)


@router.get("/{user_id}", response_model=UserOut)
async def get_user(
    user_id: int,
    session: AsyncSession = Depends(session_dependency),
) -> User:
    # mock API call
    await asyncio.sleep(0.5)
    user = await crud.get_user(session, user_id)
    if user:
        return user

    # with open(...) as file:
    #     file.read()
    #     file.write()
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User #{user_id} not found!",
    )


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user_id: int,
    session: AsyncSession = Depends(session_dependency),
) -> None:
    return await crud.delete_user(session, user_id)
