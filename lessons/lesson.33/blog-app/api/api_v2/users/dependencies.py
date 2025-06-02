from typing import Annotated, AsyncGenerator

from pydantic import PositiveInt
from fastapi import Depends, Path, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v2.users.crud import UsersCRUD
from models import User
from models.db_async import async_session


async def get_async_session() -> AsyncGenerator[AsyncSession]:
    async with async_session() as session:
        yield session


def users_crud(
    session: Annotated[
        AsyncSession,
        Depends(get_async_session),
    ],
) -> UsersCRUD:
    return UsersCRUD(session)


async def get_user_by_id(
    user_id: Annotated[PositiveInt, Path],
    crud: Annotated[
        UsersCRUD,
        Depends(users_crud),
    ],
) -> User:
    user: User | None = await crud.get_by_id(user_id)
    if user is not None:
        return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User #{user_id} not found",
    )
