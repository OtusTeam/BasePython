"""
test items
"""
def test_item_list(client):
    """
    test item list
    :param client:
    :return:
    """
    response = client.get('/items/')
    assert response.status_code == 200


def test_get_products(client):
    """
    test get products
    :param client:
    :return:
    """
    response = client.get('/products/')
    assert response.status_code == 200