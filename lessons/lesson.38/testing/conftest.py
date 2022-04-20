from flask.testing import FlaskClient
from pytest import fixture

from app import app


@fixture
def client() -> FlaskClient:
    app.config.update(SERVER_NAME="server")
    with app.test_client() as test_client:  # type: FlaskClient
        with app.app_context():
            yield test_client
