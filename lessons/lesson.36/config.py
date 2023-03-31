from os import getenv

SQLALCHEMY_DATABASE_URI = getenv(
    "SQLALCHEMY_DATABASE_URI",
    "postgresql+psycopg2://username:passwd@localhost:5432/blog",
)


class Config:
    DEBUG = False
    TESTING = False
    ENV = ""
    SECRET_KEY = "qwert12e12y"
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_ECHO = False
    WTF_CSRF_TIME_LIMIT = 600


class ProductionConfig(Config):
    ENV = "production"


class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True
    SQLALCHEMY_ECHO = True


class TestingConfig(Config):
    ENV = "testing"
    TESTING = True
    SQLALCHEMY_ECHO = True
