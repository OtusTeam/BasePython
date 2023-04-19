"""
conftest
"""
import pytest
from flask.testing import FlaskClient

from main import app


@pytest.fixture
def client() -> FlaskClient:
    """
    FlaskClient
    :return:
    """
    with app.test_client() as test_client:
        yield test_client
