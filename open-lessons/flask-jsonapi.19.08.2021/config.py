class BaseConfig:
    SQLALCHEMY_DATABASE_URI = "sqlite:////:memory:"
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # swagger

    OPENAPI_URL_PREFIX = "/docs"
    OPENAPI_VERSION = "2.0.0"
    OPENAPI_SWAGGER_UI_PATH = "/"
    OPENAPI_SWAGGER_UI_VERSION = "3.45.0"


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///./flask-jsonapi.db"
