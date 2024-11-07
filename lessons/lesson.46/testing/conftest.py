import pytest
from main import app


@pytest.fixture
def client():
    app.testing = True
    return app.test_client()
