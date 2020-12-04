from time import time
from pytest import fixture
from flask import url_for
from app import app
from models.product import Product


@fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            yield client


def test_add_product(client):
    url = url_for("product_app.product_add")
    product_name = f"Laptop{time()}"
    Product.query.filter_by(name=product_name).delete()
    data = {
        "product-name": product_name,
        "is-new": "",
    }
    response = client.post(url, data=data, mimetype="application/x-www-form-urlencoded")
    assert response.status_code < 400
    product = Product.query.filter_by(name=product_name).one()
    assert product.is_new is False
