from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker

from config import settings

engine = create_engine(
    url=settings.db.url,
    echo=settings.db.echo,
    pool_size=settings.db.pool_size,
    max_overflow=settings.db.max_overflow,
)


session_factory = sessionmaker(bind=engine)


def set_sqlite_pragma(dbapi_connection, connection_record):
    """
    Enables foreign key enforcement for SQLite connections.
    """
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


if settings.db.driver_sync.startswith("sqlite://"):
    event.listen(
        engine,
        "connect",
        set_sqlite_pragma,
    )
