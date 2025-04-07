def test_index(client):
    response = client.get('/')
    assert 200 == response.status_code


def test_users(client):
    response = client.get('/api/v1/authors/')
    assert 200 == response.status_code
