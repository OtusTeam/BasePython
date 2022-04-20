from http import HTTPStatus

from flask import url_for


def test_reset_products(client):
    url = url_for("products_app.reset")
    response = client.post(url)
    assert response.status_code == HTTPStatus.OK, response.data
    assert response.json == {"ok": True}
