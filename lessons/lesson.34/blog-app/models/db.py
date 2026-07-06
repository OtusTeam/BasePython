import sqlite3

from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker

from config import settings

engine = create_engine(
    url=settings.db.url,
    echo=settings.db.sqla.echo,
    pool_size=settings.db.sqla.pool_size,
    max_overflow=settings.db.sqla.max_overflow,
)

session_factory = sessionmaker(
    bind=engine,
)


@event.listens_for(engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, sqlite3.Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()
