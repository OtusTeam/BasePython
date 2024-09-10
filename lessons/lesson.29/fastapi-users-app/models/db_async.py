from sqlalchemy.exc import SQLAlchemyError

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

import config

async_engine = create_async_engine(
    url=config.DB_ASYNC_URL,
    echo=config.DB_ECHO,
    pool_size=config.SQLA_POOL_SIZE,
    max_overflow=config.SQLA_MAX_OVERFLOW,
)

async_session = async_sessionmaker(
    bind=async_engine,
    expire_on_commit=False,
    autoflush=False,
)


async def get_async_session():
    async with async_session() as session:
        try:
            yield session
        except SQLAlchemyError:
            await session.rollback()
