DB_URL = "postgresql+pg8000://username:passwd!@localhost:5432/blog"
# DB_ASYNC_URL = "postgresql+asyncpg://username:passwd!@localhost:5432/blog"
DB_ASYNC_URL = DB_URL.replace("pg8000", "asyncpg")
DB_ECHO = True
