from os import getenv

SQLA_DB_URL = "postgresql+psycopg://postgres:password@localhost:5432/postgres"
SQLA_DB_ECHO = False

if getenv("SQLA_DB_ECHO") == "1":
    SQLA_DB_ECHO = True
