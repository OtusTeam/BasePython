DB_URL = "postgresql+psycopg2://username:passwd!@localhost:5432/blog"
# DB_ASYNC_URL = "postgresql+asyncpg://username:passwd!@localhost:5432/blog"
DB_ASYNC_URL = DB_URL.replace("psycopg2", "asyncpg")
DB_ECHO = False
DB_POOL_SIZE = 90
DB_MAX_OVERFLOW = 10
