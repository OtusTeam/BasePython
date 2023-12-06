from os import getenv

SQLALCHEMY_DATABASE_URI = getenv(
    "SQLALCHEMY_DATABASE_URI",
    "postgresql+psycopg://user:example@localhost:5432/blog",
)


class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = ""
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI


class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = "..."  # read from secret file


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = "ad02b0412924a5948092f0b2bb96eadf27e0722f"


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
