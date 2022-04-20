from http import HTTPStatus

from flask import url_for


def test_root(client):
    url = url_for("hello_world")
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK, response.data
    assert b"Hello, World" in response.data


def test_get_item(client):
    item_id = 42
    url = url_for("get_item", item_id=item_id)
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK, response.data
    assert response.json == {"item_id": item_id}
