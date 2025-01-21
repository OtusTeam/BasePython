from pytest import fixture
from fastapi.testclient import TestClient
from main import app


@fixture
def client():
    app_client = TestClient(app)
    return app_client
