"""
TEst main
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
    url = url_for('get_item', item_id=2)
    # url = '/items/2/'
    response = client.get(url)
    assert response.status_code == 200
    assert response.json['item']['id'] == 2
