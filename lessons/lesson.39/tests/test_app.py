from flask import url_for


def test_get_item(client):
    item_id = 42
    url = url_for("get_item", item_id=item_id)
    response = client.get(url)
    data = response.json
    assert data == {"item_id": item_id}
