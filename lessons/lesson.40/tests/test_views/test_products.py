from time import time

from flask import url_for

from models import Product


def test_reset_products(client):
    url = url_for("products_app.reset")
    response = client.post(url)
    data = response.json
    assert data == {"ok": True}


def test_add_product(client):
    url = url_for("products_app.add")
    product_name = f"product_{time()}"
    is_new = True
    form = {"name": product_name, "is_new": is_new}
    response = client.post(url, data=form)
    assert response.status_code < 400
    product = Product.query.filter_by(name=product_name).one()
    assert product.is_new == is_new
    assert product.id > 0


def test_add_product_already_exists(client):
    url = url_for("products_app.add")
    product_name = f"product_{time()}"
    is_new = True
    form = {"name": product_name, "is_new": is_new}
    response = client.post(url, data=form)
    assert response.status_code < 400
    response = client.post(url, data=form)
    assert response.status_code >= 400
    assert b"probably name is not unique" in response.data
