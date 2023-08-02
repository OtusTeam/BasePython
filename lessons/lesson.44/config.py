import os
from os import getenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

PASSWD = os.getenv('POSTGRES_PASSWORD', 'passwd')

DEFAULT_DB_URL = f"postgresql://username:{PASSWD}@0.0.0.0:5432/blog"

SQLALCHEMY_DATABASE_URI = getenv(
    "SQLALCHEMY_DATABASE_URI",
    DEFAULT_DB_URL,
)


class Config:
    TESTING = False
    DEBUG = False
    SECRET_KEY = "e4de2b570761b7a6ce1efb624f848425"
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI


class ProductionConfig(Config):
    SECRET_KEY = "bc8e68da85e667ba4c8682e2bd7706a3"
    SQLALCHEMY_DATABASE_URI = f"postgresql://username:{PASSWD}@0.0.0.0:5432/blog"


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f"postgresql://username:{PASSWD}@0.0.0.0:5432/blog"


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = f"postgresql://username:{PASSWD}@postgres:5432/blog"
