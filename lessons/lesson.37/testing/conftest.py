from flask.testing import FlaskClient

from pytest import fixture

from main import app


@fixture
def client() -> FlaskClient:
    app.config.update(WTF_CSRF_ENABLED=False)
    app.config.update(SERVER_NAME="server.org")
    # pylint: disable=redefined-outer-name
    with app.test_client() as client:  # type: FlaskClient
        with app.app_context():
            yield client
