import sys

import pytest

module_app = pytest.importorskip("homework_05.app")


@pytest.fixture
def client():
    try:
        app = module_app.app
    except AttributeError:
        raise pytest.fail("skip testing homework_05 due to lack of FastAPI `app` in the `app.py`")

    from fastapi.testclient import TestClient

    return TestClient(app)


def test_visit_index(client):
    response = client.get("/")
    assert response.status_code == 200


def test_visit_about(client):
    response = client.get("/about/")
    assert response.status_code == 200


def test_nav_present(client):
    response = client.get("/")
    assert b'<nav class="navbar' in response.content
    assert b'</nav>' in response.content


def test_meta_viewport_present(client):
    response = client.get("/")
    assert b'<meta name="viewport"' in response.content
