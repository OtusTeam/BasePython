from flask import url_for
from pytest import fixture

from app import app


@fixture
def client():
    with app.test_client() as test_client:
        with app.app_context():
            yield test_client


def test_reset_products(client):
    url = url_for("products_app.reset")
    res = client.delete(url)
    data = res.json
    assert data == {"ok": True}

