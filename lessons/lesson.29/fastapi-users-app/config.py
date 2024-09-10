from os import getenv

DB_URL = "postgresql+psycopg://user:password@localhost:5432/blog"
DB_ASYNC_URL = "postgresql+asyncpg://user:password@localhost:5432/blog"
DB_ECHO = getenv("DB_ECHO", False)
if DB_ECHO and DB_ECHO.isdigit():
    DB_ECHO = int(DB_ECHO)
DB_ECHO = bool(DB_ECHO)

SQLA_POOL_SIZE = 50
SQLA_MAX_OVERFLOW = 10
