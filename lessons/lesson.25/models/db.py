from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
)

import config

async_engine = create_async_engine(
    url=config.DB_URL,
    echo=config.DB_ECHO,
)

async_session = async_sessionmaker(
    bind=async_engine,
    autocommit=False,
    expire_on_commit=False,
)
