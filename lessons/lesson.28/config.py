import os
from pathlib import Path

from sqlalchemy import URL

BASE_DIR = Path(__file__).resolve().parent
# SQLA_DB_URL = "postgresql+psycopg://app:m1CvzYgO2PiP6fWis6W1JfEKgnC8_At9qHCQSnS_WVo@localhost:5432/blog"
SQLA_DB_URL = URL.create(
    drivername="postgresql+psycopg",
    username="app",
    password="password",
    host="localhost",
    port=5432,
    database="blog",
)
SQLA_DB_ECHO = False

if os.getenv("SQLA_DB_ECHO") == "1":
    SQLA_DB_ECHO = True
