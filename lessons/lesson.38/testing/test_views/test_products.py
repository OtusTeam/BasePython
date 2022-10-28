"""
TEst products
"""
# import random
from flask import url_for


def test_get_item(client):
    """
    TEST get item
    :param client:
    :return:
    """
    # random_id = random.randint(1, 100)
    url = url_for('products_app.add')
    data = {
        'product-name': 'Test product name'
    }
    response = client.post(url, data=data)
    assert response.status_code < 400, response.text
    assert 'location' in response.headers
