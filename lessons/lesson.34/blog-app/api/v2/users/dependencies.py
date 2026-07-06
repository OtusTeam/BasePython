from collections.abc import AsyncGenerator
from typing import Annotated

from fastapi import Depends, Path, HTTPException, status
from pydantic import PositiveInt
from sqlalchemy.ext.asyncio import AsyncSession

from api.v2.users.crud import Crud
from models import User
from models.db_async import async_session


async def get_async_session() -> AsyncGenerator[AsyncSession]:
    async with async_session() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise


GetAsyncSession = Annotated[
    AsyncSession,
    Depends(get_async_session),
]


def get_crud(
    session: GetAsyncSession,
) -> Crud:
    return Crud(session)


GetCrud = Annotated[
    Crud,
    Depends(get_crud),
]


async def get_user(
    user_id: Annotated[PositiveInt, Path()],
    crud: GetCrud,
) -> User:
    user = await crud.get_user(user_id)
    if user is not None:
        return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User #{user_id} not found",
    )


GetUser = Annotated[
    User,
    Depends(get_user),
]
