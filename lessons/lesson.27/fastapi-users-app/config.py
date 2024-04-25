DB_ENGINE = "psycopg"
DB_ENGINE_ASYNC = "asyncpg"
# DB_ENGINE = "pg8000"
DB_USER = "user"
DB_PASSWORD = "example"
DB_NAME = "blog"
DB_HOST = "localhost"
DB_PORT = 5432

DB_URL = f"postgresql+{DB_ENGINE}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
DB_URL_ASYNC = f"postgresql+{DB_ENGINE_ASYNC}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# DB_ECHO = True
DB_ECHO = False

DB_POOL_SIZE = 50
DB_MAX_OVERFLOW = 10

API_V1_PREFIX = "/v1"
API_V2_PREFIX = "/v2"
API_PREFIX = "/api"
