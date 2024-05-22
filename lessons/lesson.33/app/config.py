import os

SQLALCHEMY_DATABASE_URI = os.environ.get(
    'DATABASE_URI',
)
SQLALCHEMY_ECHO = False
