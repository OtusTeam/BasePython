import pytest
from django.urls import reverse


# @pytest.mark.django_db
def test_index_view(client):
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200
    assert "<h1> OTUS blog </h1>" in response.content.decode('utf-8')


@pytest.mark.django_db
def test_post_list_view(client, author, post):
    url = reverse('post_list')
    response = client.get(url)

    assert response.status_code == 200

    assert post.title.encode("utf-8") in response.content
    assert author.name.encode("utf-8") in response.content
