import os
from sqlalchemy.engine import URL

DEBUG = False
if os.getenv("DEBUG") or True:
    DEBUG = True

SQLA_ECHO = DEBUG
SQLA_URL = URL.create(
    drivername="postgresql+psycopg",
    username="postgres",
    password="password",
    host="localhost",
    port=5432,
    database="postgres",
)
