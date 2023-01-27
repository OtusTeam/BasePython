"""
Test main
"""

import random
import time
from models import db, Product


def test_get_item(client):
    """
    Test get item
    :param client:
    :return:
    """
    random_id = random.randint(1,100)
    url = f'/items/{random_id}/'
    response = client.get(url)
    assert response.status_code == 200

    assert response.json['item']['id'] == random_id


def test_add_product(client):
    """
    test add product
    :param client:
    :return:
    """
    url = '/products/add/'
    name = f'Test product {time.time}'
    data = {
        'product-name': name,
        'description': 'Test description'
    }

    product = db.session.query(Product).filter_by(name=name).one_or_none()

    assert product is None

    response = client.post(url, data=data)
    assert response.status_code == 302, response.text

    product = db.session.query(Product).filter_by(name=name).one_or_none()

    assert product.description == 'Test description'