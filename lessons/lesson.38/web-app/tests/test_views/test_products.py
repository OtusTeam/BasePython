from flask import url_for
from pytest import fixture
from time import time

from web_app.models import Product
from app import app


@fixture
def client():
    with app.test_client() as test_client:
        with app.app_context():
            yield test_client


def test_add_product(client):
    product_name = f"product_{time()}"
    # assert Product.query.filter_by(name=product_name).count() == 0
    url = url_for("products_app.add")
    data = {
        "product-name": product_name,
    }
    res = client.post(url, data=data, mimetype="application/x-www-form-urlencoded")

    assert res.status_code < 400

    product = Product.query.filter_by(name=product_name).one()
    assert product.name == product_name


def test_add_product_already_exists(client):
    product_name = f"product_{time()}"
    url = url_for("products_app.add")
    data = {
        "product-name": product_name,
    }
    res = client.post(url, data=data, mimetype="application/x-www-form-urlencoded")

    assert res.status_code < 400

    res = client.post(url, data=data, mimetype="application/x-www-form-urlencoded")
    assert res.status_code >= 500
