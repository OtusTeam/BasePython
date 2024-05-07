import os

SQLALCHEMY_DATABASE_URI = os.environ.get(
    "SQLALCHEMY_DATABASE_URI",
    # "postgresql+psycopg://user:example@postgres:5432/shop",
    "postgresql+psycopg://user:example@localhost:5432/shop",
)
SQLALCHEMY_ECHO = False
