def test_hello(client):
    response = client.get('/products/')
    assert response.status_code == 200