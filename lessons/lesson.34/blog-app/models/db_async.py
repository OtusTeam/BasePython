import sqlite3

from sqlalchemy import event
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from config import settings

async_engine = create_async_engine(
    url=settings.db.async_url,
    echo=settings.db.sqla.echo,
    pool_size=settings.db.sqla.pool_size,
    max_overflow=settings.db.sqla.max_overflow,
)

async_session = async_sessionmaker(
    bind=async_engine,
    expire_on_commit=False,
    autoflush=False,
    autocommit=False,
)


@event.listens_for(async_engine.sync_engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, sqlite3.Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()
