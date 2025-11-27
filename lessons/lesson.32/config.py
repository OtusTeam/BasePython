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
SQLA_ASYNC_URL = URL.create(
    drivername="postgresql+asyncpg",
    username=PG_USER,
    password=PG_PASSWORD,
    host=PG_HOST,
    port=PG_PORT,
    database=PG_DB,
)

SQLA_ECHO = False
if getenv("SQLA_ECHO") == "1":
    SQLA_ECHO = True


sqla_naming_convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}
