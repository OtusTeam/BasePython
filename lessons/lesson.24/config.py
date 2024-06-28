from os import getenv

DB_URL = "postgresql+psycopg://user:password@localhost:5432/blog"
DB_ECHO = getenv("DB_ECHO", False)
if DB_ECHO and DB_ECHO.isdigit():
    DB_ECHO = int(DB_ECHO)
DB_ECHO = bool(DB_ECHO)
