def test_item_details_status_code(client):
    response = client.get(f'/items/{1}/')
    assert response.status_code == 200


def test_item_details_data(client):
    response = client.get(f'/items/{1}/')
    data = response.json

    result = {
        "data": {
            "id": 1,
            "name": "single",
        }
    }
    assert data == result
