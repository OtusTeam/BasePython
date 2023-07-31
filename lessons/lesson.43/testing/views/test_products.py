def test_products_status_code(client):
    response = client.get(f'/products/')
    assert response.status_code == 200


