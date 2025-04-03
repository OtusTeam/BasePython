PG_DB = "blog"
PG_USER = "app"
PG_PASSWORD = "password"
PG_HOST = "localhost"
PG_PORT = 5432

SQLA_PG_ENGINE = "psycopg"
SQLA_PG_ASYNC_ENGINE = "asyncpg"

SQLA_PG_URL = (
    f"postgresql+{SQLA_PG_ENGINE}://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}"
)
SQLA_PG_ASYNC_URL = (
    f"postgresql+{SQLA_PG_ASYNC_ENGINE}://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}"
)
SQLA_ECHO = True

SQLA_NAMING_CONVENTION = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}
