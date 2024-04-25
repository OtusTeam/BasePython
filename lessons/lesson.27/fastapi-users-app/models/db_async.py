from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
)

import config

async_engine = create_async_engine(
    url=config.DB_URL_ASYNC,
    echo=config.DB_ECHO,
    pool_size=config.DB_POOL_SIZE,
    max_overflow=config.DB_MAX_OVERFLOW,
)

async_session = async_sessionmaker(
    bind=async_engine,
    autocommit=False,
    expire_on_commit=False,
)
