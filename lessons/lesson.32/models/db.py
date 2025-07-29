from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker

import config

engine = create_engine(
    url=config.db_url,
    echo=config.db_echo,
)

session_factory = sessionmaker(
    bind=engine,
    autocommit=False,
)


def set_foreign_keys_on_for_sqlite(dbapi_con, connection_record):
    cursor = dbapi_con.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


if config.db_url.startswith("sqlite://"):
    event.listen(
        engine,
        "connect",
        set_foreign_keys_on_for_sqlite,
    )
