"""
TEst products
"""
from time import time
from flask import url_for

from models import Product


def test_add_product(client):
    """
    TEST get item
    :param client:
    :return:
    """
    product_name = f'product{time()}'
    url = url_for('products_app.add')
    data = {
        'product-name': product_name
    }
    product = Product.query.filter_by(name=product_name).one_or_none()
    assert product is None
    response = client.post(url, data=data)
    assert response.status_code < 400, response.text
    assert 'location' in response.headers
    product = Product.query.filter_by(name=product_name).one_or_none()
    assert product.name == product_name
