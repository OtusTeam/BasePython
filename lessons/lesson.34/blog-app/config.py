import os
from sqlalchemy.engine import URL

DEBUG = False
if os.getenv("DEBUG"):
    DEBUG = True

SQLA_POOL_SIZE = 50
SQLA_MAX_OVERFLOW = 0
SQLA_ECHO = DEBUG
SQLA_URL = URL.create(
    drivername="postgresql+psycopg",
    username="postgres",
    password="password",
    host="localhost",
    port=5432,
    database="postgres",
)
SQLA_ASYNC_URL = URL.create(
    drivername="postgresql+psycopg",
    # drivername="postgresql+asyncpg",
    username="postgres",
    password="password",
    host="localhost",
    port=5432,
    database="postgres",
)
