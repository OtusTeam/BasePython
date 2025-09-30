from sqlalchemy import event

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
)

from config import settings

async_engine = create_async_engine(
    url=settings.db.async_url,
    echo=settings.db.echo,
    pool_size=settings.db.pool_size,
    max_overflow=settings.db.max_overflow,
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


if settings.db.driver_async.startswith("sqlite://"):
    event.listen(
        async_engine.sync_engine,
        "connect",
        set_sqlite_pragma,
    )
