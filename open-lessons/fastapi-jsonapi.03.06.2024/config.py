from pathlib import Path

CURRENT_FILE = Path(__file__).resolve()
PROJECT_DIR = CURRENT_FILE.parent
DB_URL = f"sqlite+aiosqlite:///{PROJECT_DIR}/db.sqlite3"
# DB_ECHO = False
DB_ECHO = True
