from os import getenv

DB_SYNC_URL = "postgresql+psycopg://user:password@localhost:5432/blog"
DB_ASYNC_URL = "postgresql+asyncpg://user:password@localhost:5432/blog"
DB_ECHO = getenv("DB_ECHO", False)
if DB_ECHO and DB_ECHO.isdigit():
    DB_ECHO = int(DB_ECHO)
DB_ECHO = bool(DB_ECHO)

DB_POOL_SIZE = 50
DB_MAX_OVERFLOW = 0
