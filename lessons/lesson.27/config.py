from os import getenv

DB_FILENAME = "blog.db"
DB_URL = f"sqlite:///{DB_FILENAME}"
DB_ECHO = getenv("SQLA_ECHO", None) == "1"
