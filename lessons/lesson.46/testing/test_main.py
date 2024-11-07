def test_sum():
    assert 1 + 2 == 3


def test_hello(client):
    response = client.get('/')
    assert response.status_code == 200

def test_about(client):
    response = client.get('/about/some-str/')
    assert response.status_code == 200
