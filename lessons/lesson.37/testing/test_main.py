from random import randint

from flask import url_for


def test_get_item(client):
    item_id = randint(1, 1000)
    url = url_for("get_item", item_id=item_id)
    response = client.get(url)

    data = response.json

    assert data == {
        "item": {"id": item_id},
    }
