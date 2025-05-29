from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker

import config

engine = create_engine(
    url=config.DB_URL_SYNC,
    echo=config.DB_ECHO,
)

session_factory = sessionmaker(bind=engine)


def set_foreign_keys_on_for_sqlite(dbapi_con, connection_record):
    cursor = dbapi_con.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


if config.DB_URL_SYNC.startswith("sqlite://"):
    event.listen(
        engine,
        "connect",
        set_foreign_keys_on_for_sqlite,
    )
