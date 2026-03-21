import sqlite3

from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker

import config

engine = create_engine(
    url=config.DB_URL,
    echo=config.DB_ECHO,
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
