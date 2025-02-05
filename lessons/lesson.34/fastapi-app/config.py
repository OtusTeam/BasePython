convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

db_url = "postgresql+psycopg://app:apppassword@localhost:5432/blog"
db_async_url = "postgresql+asyncpg://app:apppassword@localhost:5432/blog"
db_echo = False
db_pool_size = 50
db_max_overflow = 0
