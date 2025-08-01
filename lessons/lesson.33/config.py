db_url = "postgresql+psycopg://app:password@localhost:5428/blog"
db_async_url = "postgresql+asyncpg://app:password@localhost:5428/blog"
db_echo = False

sqla_pool_size = 50
sqla_max_overflow = 0

users_api_url = "http://127.0.0.1:5000/user-info/{user_id}"
