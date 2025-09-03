from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker

import config

engine = create_engine(
    url=config.db_url,
    echo=config.db_echo,
)


Session = sessionmaker(bind=engine)


def set_sqlite_pragma(dbapi_connection, connection_record):
    """
    Enables foreign key enforcement for SQLite connections.
    """
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


if config.db_url.startswith("sqlite://"):
    event.listen(
        engine,
        "connect",
        set_sqlite_pragma,
    )
