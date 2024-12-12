from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_get_all_user():
    response = client.get("/users/")
    assert response.status_code == 200
    assert response.json() == []


def test_create_user():
    new_user = {
        "username": "test",
        "password": "test"
    }
    response = client.post("/users/", json=new_user)
    assert response.status_code == 200
    res = response.json()


def test_get_user():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "username": "test", "password": "test"}