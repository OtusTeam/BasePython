import pytest
from django.urls import reverse


def test_index_view(client):
    url = reverse("index")
    response = client.get(url)
    assert response.status_code == 200
    assert "Добро пожаловать!" in response.content.decode("utf-8")


@pytest.mark.django_db
def test_post_list_view(client, author1, author2, post1, post2):
    url = reverse("post_list")
    response = client.get(url)
    assert response.status_code == 200
    assert post1.title.encode() in response.content


@pytest.mark.django_db
def test_post_list_filter(client, author1, author2, post1, post2):
    url = reverse("post_list")
    response = client.get(url, {"rating": post2.rating})
    assert response.status_code == 200
    assert post2.title.encode() in response.content
