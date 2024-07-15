import pytest
from app import app


@pytest.fixture()
def client():
    app.config.update({
        "TESTING": True,
    })
    yield app.test_client()
