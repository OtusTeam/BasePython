from sqlalchemy import event
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
)

import config

async_engine = create_async_engine(
    url=config.db_async_url,
    echo=config.db_echo,
    max_overflow=config.sqla_max_overflow,
    pool_size=config.sqla_pool_size,
)

async_session = async_sessionmaker(
    bind=async_engine,
    expire_on_commit=False,
    autocommit=False,
)


def set_foreign_keys_on_for_sqlite(dbapi_con, connection_record):
    cursor = dbapi_con.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


if config.db_async_url.startswith("sqlite://"):
    event.listen(
        async_engine.sync_engine,
        "connect",
        set_foreign_keys_on_for_sqlite,
    )
