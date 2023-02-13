from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine,
)

from sqlalchemy.orm import sessionmaker

import config


async_engine: AsyncEngine = create_async_engine(
    url=config.DB_ASYNC_URL,
    echo=config.DB_ECHO,
)

async_session = sessionmaker(
    async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)
