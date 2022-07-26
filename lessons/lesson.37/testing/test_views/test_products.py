from http import HTTPStatus
from flask import url_for


def test_add_product(client):
    data = {
        "product-name": "Laptop",
    }
    url = url_for("products_app.add")
    response = client.post(url, data=data)

    assert response.status_code < HTTPStatus.BAD_REQUEST, response.text
    assert 'location' in response.headers
