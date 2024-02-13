from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
# DB_URL_SYNC = "postgresql+pg8000://user:example@localhost:5432/blog"
DB_URL = "postgresql+asyncpg://user:example@localhost:5432/blog"
DB_ECHO = False
# DB_ECHO = True
