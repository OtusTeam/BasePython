from collections.abc import Generator, AsyncGenerator
from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from models import session_factory, async_session


def get_session() -> Generator[Session]:
    with session_factory() as session:
        yield session


GetSession = Annotated[
    Session,
    Depends(get_session),
]


async def get_async_session() -> AsyncGenerator[AsyncSession]:
    async with async_session() as session:
        yield session


GetAsyncSession = Annotated[
    AsyncSession,
    Depends(get_async_session),
]
