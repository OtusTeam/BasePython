from pytest import fixture

from app import app


@fixture
def client():
    with app.test_client() as test_client:
        with app.app_context():
            yield test_client
