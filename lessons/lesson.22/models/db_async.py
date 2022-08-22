import asyncio

from sqlalchemy.orm import sessionmaker, joinedload, selectinload, noload
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncEngine, async_scoped_session

import config

async_engine: AsyncEngine = create_async_engine(
    config.DB_ASYNC_URL,
    echo=config.DB_ECHO,
    max_overflow=config.MAX_OVERFLOW,
    pool_size=config.POOL_SIZE,
)

async_session = sessionmaker(
    async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

Session = async_scoped_session(async_session, scopefunc=asyncio.current_task)


async def get_session_async() -> AsyncSession:
    async with Session() as session:
        yield session
