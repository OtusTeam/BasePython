def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.text == '"Hello, World!"'


def test_json(client):
    response = client.get("/json")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World in JSON!"}


def test_html(client):
    # pylint: disable=duplicate-code
    expected = """
    <html>
        <head>
            <title>Hello, World!</title>
        </head>
        <body>
            <h1>Hello, World in HTML!</h1>
        </body>
    </html>
    """
    response = client.get("/html")
    assert response.status_code == 200
    assert response.text == expected
