def test_products_list(client):
    url = "/products/"
    response = client.get(url)
    assert response.status_code == 200
