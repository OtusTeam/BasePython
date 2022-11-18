from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from pydantic import conint

from models import User
from models.db_async import get_session
from api.schemas.user import UserOut, UserIn
from . import crud
from .dependencies import get_user_by_token

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("", response_model=list[UserOut])
async def list_users(
    session: AsyncSession = Depends(get_session),
) -> list[User]:
    return await crud.get_users(session)


@router.post(
    "",
    response_model=UserOut,
    status_code=status.HTTP_201_CREATED,
)
async def create_user(
    user_in: UserIn,
    session: AsyncSession = Depends(get_session),
) -> User:
    return await crud.create_user(session, user_in)


@router.post(
    "/many",
    response_model=list[UserOut],
    status_code=status.HTTP_201_CREATED,
)
async def create_many_users(
    count: conint(ge=0, le=1000),
    session: AsyncSession = Depends(get_session),
) -> list[User]:
    return await crud.create_many_users(session, count)


@router.get("/me", response_model=UserOut)
async def get_me(
    user: User = Depends(get_user_by_token),
) -> User:
    return user


@router.get("/{user_id}", response_model=UserOut)
async def get_user(
    user_id: int,
    session: AsyncSession = Depends(get_session),
) -> User:
    user = await crud.get_user_by_id(session, user_id)
    if user:
        return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"user #{user_id} doesn't exist!",
    )


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_user(
    user_id: int,
    session: AsyncSession = Depends(get_session),
):
    await crud.delete_user(session, user_id)
