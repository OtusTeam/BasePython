from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker

import config

engine_params = dict(
    echo_pool=config.DB_ECHO_POOL,
    pool_size=config.DB_POOL_SIZE,
    max_overflow=config.DB_MAX_OVERFLOW,
    echo=config.DB_ECHO,
)

engine = create_engine(
    url=config.DB_URL,
    **engine_params,
)

async_engine = create_async_engine(
    url=config.DB_URL_ASYNC,
    **engine_params,
)

session = sessionmaker(
    bind=engine,
    autocommit=False,
    expire_on_commit=False,
)

async_session = async_sessionmaker(
    bind=async_engine,
    autocommit=False,
    expire_on_commit=False,
)
