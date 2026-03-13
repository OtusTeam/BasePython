from os import getenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DB_PATH = BASE_DIR / "blog.db"

DB_URL = f"sqlite:///{DB_PATH}"
DB_ECHO = getenv("DB_ECHO") == "1"
