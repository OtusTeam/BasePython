from os import getenv

from sqlalchemy import URL

DB_FILENAME = "blog.db"
DB_URL = f"sqlite:///{DB_FILENAME}"
DB_ECHO = getenv("SQLA_ECHO", None) == "1"

SQLA_URL = URL.create(
    drivername="postgresql+psycopg",
    username="postgres",
    password="password",  # getenv("PG_PASSWORD")
    host="localhost",
    port=5432,
    database="postgres",
)

SQLA_ASYNC_URL = SQLA_URL.set(
    # drivername="postgresql+asyncpg",
)
