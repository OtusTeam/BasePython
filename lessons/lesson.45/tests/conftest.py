from pytest import fixture
from app import app


@fixture
def client():
    app.config.update({
        "TESTING": True,
    })
    result = app.test_client()
    yield result
