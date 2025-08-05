from sqlalchemy import event
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
)

from config import settings

async_engine = create_async_engine(
    url=str(settings.db.async_url),
    echo=settings.db.echo,
    max_overflow=settings.db.max_overflow,
    pool_size=settings.db.pool_size,
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


if settings.db.async_url.scheme.startswith("sqlite"):
    event.listen(
        async_engine.sync_engine,
        "connect",
        set_foreign_keys_on_for_sqlite,
    )
