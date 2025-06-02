DB_URL_SYNC = f"postgresql+psycopg://app:password@localhost:5425/blog"
# DB_URL_ASYNC = f"postgresql+psycopg://app:password@localhost:5425/blog"
DB_URL_ASYNC = f"postgresql+asyncpg://app:password@localhost:5425/blog"

DB_ECHO = False

SQLA_POOL_SIZE = 50
SQLA_MAX_OVERFLOW = 0
