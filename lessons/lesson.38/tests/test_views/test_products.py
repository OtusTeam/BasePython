from flask import url_for


def test_reset_products(client):
    url = url_for("products_app.reset")
    response = client.post(url)
    data = response.json
    assert data == {"ok": True}
