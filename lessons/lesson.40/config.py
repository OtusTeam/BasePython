from os import getenv

SQLALCHEMY_DATABASE_URI = getenv(
    "SQLALCHEMY_DATABASE_URI",
    "postgresql+psycopg2://app:password@localhost/shop",
)


class Config(object):
    TESTING = False
    DEBUG = False
    ENV = "development"
    SECRET_KEY = "\xe4X\xb2\xd6\xf2\x94\xca\xd3m\xccMM\x07l"
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    ENV = "production"


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    ENV = "testing"
    TESTING = True
