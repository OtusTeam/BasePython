from collections.abc import AsyncIterator
from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from models import async_session


async def session_dependency() -> AsyncIterator[AsyncSession]:
    async with async_session() as session:
        yield session


AsyncSessionDep = Annotated[
    AsyncSession,
    Depends(session_dependency),
]
