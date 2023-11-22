from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker, scoped_session

import config

async_engine = create_async_engine(
    url=config.DB_URL,
    echo_pool=config.DB_ECHO,
    pool_size=config.DB_POOL_SIZE,
    max_overflow=config.DB_MAX_OVERFLOW,
)

session_factory = async_sessionmaker(
    bind=async_engine,
    autoflush=False,
    # autocommit=False,
    expire_on_commit=False,
)


async def session_dependency():
    async with session_factory() as session:
        yield session
