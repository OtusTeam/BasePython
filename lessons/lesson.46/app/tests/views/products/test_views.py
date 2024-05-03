def test_products(client):
    url = "/products/"
    response = client.get(url)
    assert response.status_code == 200
