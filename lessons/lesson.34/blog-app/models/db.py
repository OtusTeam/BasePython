from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker

from config import settings

engine = create_engine(
    url=settings.db.url_sync,
    echo=settings.db.echo,
    pool_size=settings.db.pool_size,
    max_overflow=settings.db.max_overflow,
)

session_factory = sessionmaker(bind=engine)


def set_foreign_keys_on_for_sqlite(dbapi_con, connection_record):
    cursor = dbapi_con.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


if "sqlite" in settings.db.dialect:
    event.listen(
        engine,
        "connect",
        set_foreign_keys_on_for_sqlite,
    )
