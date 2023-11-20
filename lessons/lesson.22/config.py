from pathlib import Path

BASE_DIR = Path(__file__).parent
# db_file_path = BASE_DIR / "blog.db"

# DB_URL = f"sqlite:///{db_file_path}"
# DB_URL = "postgresql+pg8000://user:example@localhost:5432/blog"
DB_URL = "postgresql+asyncpg://user:example@localhost:5432/blog"
# DB_ECHO = False
DB_ECHO = True
