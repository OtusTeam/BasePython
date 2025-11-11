from os import getenv

from sqlalchemy import URL

PG_HOST = "localhost"
PG_PORT = 5432
PG_DB = "blog"
PG_USER = "postgres"
PG_PASSWORD = "password"

# прямая ссылка на подключение
# это для примера
sqla_url = "postgresql+psycopg://{username}:{password}@{host}:{port}/{db}"

# это удобнее и надежнее
SQLA_URL = URL.create(
    drivername="postgresql+psycopg",
    username=PG_USER,
    password=PG_PASSWORD,
    host=PG_HOST,
    port=PG_PORT,
    database=PG_DB,
)

SQLA_ECHO = False
if getenv("SQLA_ECHO") == "1":
    SQLA_ECHO = True
