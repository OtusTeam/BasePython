# SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://user:password@localhost:5432/blog"
# SQLALCHEMY_ASYNC_DATABASE_URI = "postgresql+asyncpg://user:password@localhost:5432/blog"
SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://user:password@postgres:5432/blog"
SQLALCHEMY_ASYNC_DATABASE_URI = "postgresql+asyncpg://user:password@postgres:5432/blog"

SQLALCHEMY_ECHO = False
# # temp true!
# SQLALCHEMY_ECHO = True

SQLALCHEMY_POOL_SIZE = 50
SQLALCHEMY_MAX_OVERFLOW = 10


SQLA_NAMING_CONVENTIONS = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}
