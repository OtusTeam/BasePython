import pytest
from main import app as main_app

@pytest.fixture()
def app():
    main_app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield main_app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
