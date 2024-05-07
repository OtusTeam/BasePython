def test_index(client):
    url = "/"
    response = client.get(url)
    assert response.status_code == 200
