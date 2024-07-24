def test_products_list(client):
    response = client.get('/products/')
    assert response.status_code == 200