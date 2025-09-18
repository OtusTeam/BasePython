from sqlalchemy import event

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
)

import config

async_engine = create_async_engine(
    url=config.db_async_url,
    echo=config.db_echo,
)


async_session = async_sessionmaker(
    bind=async_engine,
    expire_on_commit=False,
)


def set_sqlite_pragma(dbapi_connection, connection_record):
    """
    Enables foreign key enforcement for SQLite connections.
    """
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


if config.db_async_url.startswith("sqlite://"):
    event.listen(
        async_engine.sync_engine,
        "connect",
        set_sqlite_pragma,
    )
