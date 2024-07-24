def test_get_items(client):
    response = client.get('/items/')
    assert response.status_code == 200
    assert response.json == {
        "items": ["a", "b"],
    }


def test_get_item_by_id(client):
    response = client.get('/items/45/')
    assert response.status_code == 200
