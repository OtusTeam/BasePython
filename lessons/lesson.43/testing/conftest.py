from flask.testing import FlaskClient
from pytest import fixture
from main import app


@fixture
def client() -> FlaskClient:
    with app.test_client() as test_client:
        with app.app_context():
            yield test_client
