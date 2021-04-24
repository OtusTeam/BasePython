from time import time

from pytest import fixture
from flask import url_for

from app import app
from my_shop.models.product import Product


@fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            yield client


def test_add_product(client):
    url_add = url_for("product_app.add")
    product_name = f"Laptop_{time()}"
    data = {
        "product-name": product_name,
    }
    resp = client.post(url_add, data=data, mimetype="application/x-www-form-urlencoded")

    assert resp.status_code < 400

    product = Product.query.filter_by(name=product_name).one()
    assert product.is_new is False
