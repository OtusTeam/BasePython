from os import getenv

# TODO: full path using pathlib
DB_PATH = "blog.db"

DB_URL = f"sqlite:///{DB_PATH}"
DB_ECHO = getenv("DB_ECHO") == "1"
