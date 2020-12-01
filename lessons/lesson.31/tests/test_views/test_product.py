from pytest import fixture

from app import app

from views.product import get_default_products


@fixture
def client():
    with app.test_client() as client:
        yield client


def test_get_default_products():
    res = get_default_products()
    assert isinstance(res, dict)
    assert all(map(lambda x: isinstance(x, int), res.keys()))


def test_recover_products(client):
    resp = client.post("/products/recover/")
    data = resp.json
    assert data == {"ok": True}
