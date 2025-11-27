from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

import config

async_engine = create_async_engine(
    url=config.SQLA_ASYNC_URL,
    echo=config.SQLA_ECHO,
)

async_session = async_sessionmaker(
    bind=async_engine,
    expire_on_commit=False,
)
