import asyncio

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_scoped_session,
)
from sqlalchemy.orm import sessionmaker

import config

engine = create_async_engine(
    url=config.ASYNC_DB_URL,
    echo=config.DB_ECHO,
    pool_size=config.DB_POOL_SIZE,
    max_overflow=config.DB_POOL_MAX_OVERFLOW,
)

session_factory = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)
AsyncScopedSession = async_scoped_session(
    session_factory,
    scopefunc=asyncio.current_task,
)


async def session_dependency() -> AsyncSession:
    async with session_factory() as session:  # type: AsyncSession
        yield session
        await session.close()


async def scoped_session_dependency() -> AsyncSession:
    session = AsyncScopedSession()
    yield session
    await session.close()
