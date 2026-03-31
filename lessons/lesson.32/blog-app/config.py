from os import getenv
from pathlib import Path

from sqlalchemy import URL

BASE_DIR = Path(__file__).resolve().parent

# DB_PATH = BASE_DIR / "blog.db"
# DB_URL = f"sqlite:///{DB_PATH}"
DB_ECHO = getenv("DB_ECHO") == "1"

# DB_URL = f"postgresql://user:password@host:port/database"

DB_URL = URL.create(
    drivername="postgresql+psycopg",
    username="postgres",
    password="password",
    host="localhost",
    port=5432,
    database="postgres",
)

DB_URL_ASYNC = URL.create(
    drivername="postgresql+asyncpg",
    username="postgres",
    password="password",
    host="localhost",
    port=5432,
    database="postgres",
)
