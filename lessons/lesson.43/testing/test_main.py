def test_main(client):
    response = client.get('/')
    assert response.status_code == 200

def test_hello_path_view(client):
    name = 'somename'
    url = f'/hello/{name}/'
    response = client.get(url)
    assert response.status_code == 200
    assert response.json == {"message": "Hello somename!"}

def test_hello_view(client):
    url = '/hello/?name=onetwothree'
    response = client.get(url)
    assert response.status_code == 200
