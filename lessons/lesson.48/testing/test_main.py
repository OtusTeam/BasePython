def test_sum():
    assert 1 + 2 == 3


def test_hello(client):
    response = client.get('/')
    assert response.status_code == 200
