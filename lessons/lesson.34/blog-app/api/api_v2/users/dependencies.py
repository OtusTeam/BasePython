from typing import Annotated, AsyncGenerator
from collections.abc import Generator

from fastapi import Depends, Path, HTTPException, status
from pydantic import PositiveInt
from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v2.users.crud import UsersCRUD
from models import async_session, User


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session


GetAsyncSession = Annotated[
    AsyncSession,
    Depends(get_async_session),
]


def get_users_crud(
    session: GetAsyncSession,
) -> UsersCRUD:
    return UsersCRUD(session)


GetUsersCRUD = Annotated[
    UsersCRUD,
    Depends(get_users_crud),
]


async def get_user_by_id(
    user_id: Annotated[
        PositiveInt,
        Path(),
    ],
    crud: GetUsersCRUD,
) -> User:
    user: User | None = await crud.get_by_id(user_id)
    if user:
        return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User #{user_id} not found",
    )
