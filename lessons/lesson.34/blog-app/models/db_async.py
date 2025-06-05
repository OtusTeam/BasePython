from sqlalchemy import event
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from config import settings

async_engine = create_async_engine(
    url=settings.db.url_async,
    echo=settings.db.echo,
    pool_size=settings.db.pool_size,
    max_overflow=settings.db.max_overflow,
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


if "sqlite" in settings.db.dialect:
    event.listen(
        async_engine.sync_engine,
        "connect",
        set_foreign_keys_on_for_sqlite,
    )
