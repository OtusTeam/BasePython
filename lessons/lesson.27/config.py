from os import getenv


SQLALCHEMY_DATABASE_URI = getenv(
    "SQLALCHEMY_DATABASE_URI",
    "postgresql+psycopg2://app:password@localhost/shop",
)


class Config:
    DEBUG = False
    TESTING = False
    ENV = "development"

    SECRET_KEY = "\xe4X\xb2\xd6\xf2\x94\xca\xd3m\xccMM\x07l"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI


class ProductionConfig(Config):
    ENV = "production"
    SECRET_KEY = "B4hX\x13'\xd3N|K\xb9\x8b\xad\x86\xac0"


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
