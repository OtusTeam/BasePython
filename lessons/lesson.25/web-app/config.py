from os import getenv

SQLALCHEMY_DATABASE_URI = getenv("SQLALCHEMY_DATABASE_URI", "postgresql://user:password@localhost:5432/app")


class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI


class ProductionConfig(Config):
    """"""


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True


class TestingConfig(Config):
    TESTING = True
