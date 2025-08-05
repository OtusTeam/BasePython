from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker

from config import settings

engine = create_engine(
    url=str(settings.db.url),
    echo=settings.db.echo,
    max_overflow=settings.db.max_overflow,
    pool_size=settings.db.pool_size,
)

session_factory = sessionmaker(
    bind=engine,
    autocommit=False,
)


def set_foreign_keys_on_for_sqlite(dbapi_con, connection_record):
    cursor = dbapi_con.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


if settings.db.url.scheme.startswith("sqlite"):
    event.listen(
        engine,
        "connect",
        set_foreign_keys_on_for_sqlite,
    )
