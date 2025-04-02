def test_index(client):
    response = client.get('/')
    assert 200 == response.status_code
