from time import time

from flask import url_for

from models import Product


def test_create_product(client):
    url = url_for("products_app.add")
    product_name = f"product_{time()}"
    form = {"product-name": product_name}
    response = client.post(url, data=form)
    assert response.status_code < 400
    product = Product.query.filter_by(name=product_name).one()
    assert product.id > 0


def test_add_product_already_exists(client):
    url = url_for("products_app.add")
    product_name = f"product_{time()}"
    form = {"product-name": product_name}
    response = client.post(url, data=form)
    assert response.status_code < 400
    response = client.post(url, data=form)
    assert response.status_code >= 400
    assert b"probably the name is not unique" in response.data


def test_add_product_dont_provide_name(client):
    url = url_for("products_app.add")
    response = client.post(url)
    assert response.status_code >= 400
    assert b"provide product name" in response.data
