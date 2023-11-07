def test_get_item_by_id_status_code(client):
    url = '/items/25/'
    response = client.get(url)
    assert response.status_code == 200


def test_get_item_by_id_data(client):
    url = '/items/25/'
    response = client.get(url)
    expected_response = {"data": {"id": 25}}
    assert response.json == expected_response
