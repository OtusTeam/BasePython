from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

import config

async_engine = create_async_engine(
    url=config.SQLA_DB_URL_ASYNC,
    echo=config.SQLA_DB_ECHO,
    pool_size=config.SQLA_POOL_SIZE,
    max_overflow=config.SQLA_MAX_OVERFLOW,
)


async_session = async_sessionmaker(
    bind=async_engine,
    expire_on_commit=False,
)
