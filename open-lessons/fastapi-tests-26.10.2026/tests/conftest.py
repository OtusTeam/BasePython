import pytest
from starlette.testclient import TestClient
from sqlalchemy.orm import sessionmaker

from bookshelf.config.settings import settings as default_settings, Settings
from bookshelf.core.db import managed_engine
from bookshelf.main import create_app


@pytest.fixture(scope="session")
def settings():
    return default_settings


@pytest.fixture(scope="session")
def app(settings):
    return create_app(settings)


@pytest.fixture(scope="session")
def client(app):
    with TestClient(app) as client:
        yield client


@pytest.fixture(scope="module")
def db_session(settings: Settings):
    with (
        managed_engine(settings) as engine,
        sessionmaker(engine, expire_on_commit=False)() as session
    ):
        yield session


