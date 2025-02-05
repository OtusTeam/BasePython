from collections.abc import AsyncGenerator

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from models.db_async import async_session_factory
from .crud import AuthorsStorage


async def async_session_dependency() -> AsyncGenerator[AsyncSession, None, None]:
    async with async_session_factory() as session:
        yield session


def authors_crud_dependency(
    session: AsyncSession = Depends(async_session_dependency),
) -> AuthorsStorage:
    return AuthorsStorage(session=session)
