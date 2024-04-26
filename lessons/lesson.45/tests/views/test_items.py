def test_get_item(client):
    url = '/items/574/'
    response = client.get(url)
    assert response.status_code == 200

    expected = {
        "data": {
            "item_id": 574,
        }
    }
    content = response.json
    assert expected == content
