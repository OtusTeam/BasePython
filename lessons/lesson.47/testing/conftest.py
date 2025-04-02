from pytest import fixture
from fastapi.testclient import TestClient
from app import app


@fixture
def client():
    result = TestClient(app)
    return result
