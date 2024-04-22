# DB_ENGINE = "psycopg"
DB_ENGINE = "asyncpg"
# DB_ENGINE = "pg8000"
DB_USER = "user"
DB_PASSWORD = "example"
DB_NAME = "blog"
DB_HOST = "localhost"
DB_PORT = 5432

DB_URL = f"postgresql+{DB_ENGINE}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
DB_ECHO = True
# DB_ECHO = False
