from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# DB_FILE = BASE_DIR / "blog.db"
# DB_URL = f"sqlite:///{DB_FILE}"
DB_URL = f"postgresql+psycopg://app:password@localhost:5425/blog"
DB_ECHO = False
DB_ECHO = True  # temp!
