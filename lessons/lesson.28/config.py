from pathlib import Path

BASE_DIR = Path(__file__).parent
DB_FILE_PATH = BASE_DIR / "shop.db"


class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DB_FILE_PATH}"
    SQLALCHEMY_ECHO = False
    SECRET_KEY = "d28795bdb571ce24ebbfc54e29c29761701c8088ca53f7e84e59db74081adceb"


class DevelopmentConfig(Config):
    SQLALCHEMY_ECHO = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    TESTING = False
    DEBUG = False

