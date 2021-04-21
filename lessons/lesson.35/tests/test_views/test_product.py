from pytest import fixture

from flask import url_for
from app import app
from views.products import get_default_products


@fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            yield client


def test_get_default_products():
    products = get_default_products()
    assert all(map(lambda k: isinstance(k, int), products))


def test_reset_products(client):
    print("test reset runs")
    url = url_for("product_app.reset")
    res = client.delete(url)
    data = res.json
    assert data == {"ok": True}
    print("test reset done")
