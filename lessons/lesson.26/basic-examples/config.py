import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
SQLITE_FILENAME = "blog.db"
SQLITE_FILEPATH = BASE_DIR / SQLITE_FILENAME

SQLA_DB_URL = f"sqlite:///{SQLITE_FILEPATH}"
SQLA_DB_ECHO = False

if os.getenv("SQLA_DB_ECHO") == "1":
    SQLA_DB_ECHO = True
