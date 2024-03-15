import os

SQLALCHEMY_DATABASE_URI = os.environ.get(
    'SQLALCHEMY_DATABASE_URI',
    "postgresql+psycopg://user:example@localhost:5432/blog",
)
SQLALCHEMY_ECHO = False
