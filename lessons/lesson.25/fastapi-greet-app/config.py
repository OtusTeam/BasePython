from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_URL = "postgresql+psycopg://user:example@localhost:5432/blog"
DB_URL_ASYNC = "postgresql+asyncpg://user:example@localhost:5432/blog"
DB_ECHO = False
DB_ECHO_POOL = False
DB_POOL_SIZE = 50
DB_MAX_OVERFLOW = 10
# DB_ECHO = True

API_VERSION = "v.1.0.0"

API_V1_PREFIX = "/v1"
API_V2_PREFIX = "/v2"
