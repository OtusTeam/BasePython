import os

SQLALCHEMY_DATABASE_URI = os.environ.get(
    'SQLALCHEMY_DATABASE_URI',
    "postgresql+psycopg://user:example@localhost:5432/shop",
)
# SQLALCHEMY_ECHO = True
SQLALCHEMY_ECHO = False

# python -c 'import secrets; print(secrets.token_hex())'
SECRET_KEY = "6eeee0a67be22909bf04901323654afdb133e0d5b02f1fce9898145cc55f4e23"
