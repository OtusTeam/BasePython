import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
SQLITE_FILENAME = "blog.db"
SQLITE_FILEPATH = BASE_DIR / SQLITE_FILENAME

SQLA_SQLITE_DB_URL = f"sqlite:///{SQLITE_FILEPATH}"
# postgres sqlalchemy url
SQLA_DB_URL = "postgresql+psycopg://app:password@localhost:5432/blog"
SQLA_DB_URL_ASYNC = "postgresql+asyncpg://app:password@localhost:5432/blog"
SQLA_DB_ECHO = False

if os.getenv("SQLA_DB_ECHO") == "1":
    SQLA_DB_ECHO = True
