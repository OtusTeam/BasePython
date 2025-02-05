from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

import config

engine = create_async_engine(
    config.db_async_url,
    # echo=True only for debug!!
    echo=config.db_echo,
    pool_size=config.db_pool_size,
    max_overflow=config.db_max_overflow,
)


async_session_factory = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
)
