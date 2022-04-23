from time import time
from http import HTTPStatus

from flask import url_for

from models import Product


class TestAddProduct:

    def test_create_success(self, client):
        url = url_for("products_app.add")
        product_name = f"product_{time()}"
        is_new = True
        form = {"product-name": product_name, "is_new": is_new}
        response = client.post(url, data=form)
        assert response.status_code < HTTPStatus.BAD_REQUEST, response.data
        product = Product.query.filter_by(name=product_name).one()
        assert product.is_new == is_new
        assert product.id > 0

    def test_get_page(self, client):
        url = url_for("products_app.add")
        response = client.get(url)
        assert response.status_code == HTTPStatus.OK, response.data

    def test_post_invalid_form(self, client):
        url = url_for("products_app.add")
        form = {"name": "product_name"}
        response = client.post(url, data=form)
        assert response.status_code == HTTPStatus.BAD_REQUEST, response.data

    def test_product_already_exists(self, client):
        url = url_for("products_app.add")
        product_name = f"product_{time()}"
        is_new = True
        form = {"product-name": product_name, "is_new": is_new}
        response = client.post(url, data=form)
        assert response.status_code < HTTPStatus.BAD_REQUEST, response.data
        form = {"product-name": product_name, "is_new": is_new}
        response = client.post(url, data=form)
        assert response.status_code == HTTPStatus.BAD_REQUEST, response.data
        assert b"is not unique" in response.data
