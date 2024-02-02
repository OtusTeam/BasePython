from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_URL = "postgresql+psycopg://user:example@localhost:5432/blog"
# DB_ECHO = False
DB_ECHO = True
