from os import getenv

SQLALCHEMY_DATABASE_URI = getenv(
    "SQLALCHEMY_DATABASE_URI",
    "postgresql://demouser:demopass@localhost:5432/blog",
)

SECRET_KEY = getenv(
    "SECRET_KEY",
    "sgdfadfasdfasfdfas",
)


class Config:
    ENV = ""
    DEBUG = False
    TESTING = False
    SECRET_KEY = SECRET_KEY
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    ENV = "production"


class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True


class TestingConfig(Config):
    ENV = "testing"
    TESTING = True
