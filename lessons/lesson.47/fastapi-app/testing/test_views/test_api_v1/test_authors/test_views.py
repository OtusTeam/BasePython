def test_get_authors_list(client):
    response = client.get("/api/v1/authors/")
    assert response.status_code == 200
