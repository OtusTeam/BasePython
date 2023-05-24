DB_APP_PREFIX = "blog_"
DB_URL = "postgresql+pg8000://username:passwd@0.0.0.0:5432/blog"
DB_ASYNC_URL = DB_URL.replace("pg8000", "asyncpg")
# DB_ECHO = True
DB_ECHO = False
DB_POOL_SIZE = 50
DB_MAX_OVERFLOW = 10
