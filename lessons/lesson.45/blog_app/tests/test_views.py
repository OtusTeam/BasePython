import pytest
from django.urls import reverse
from blog_app.models import Post, Author


def test_index_view(client):
    """ Тест для проверки главной страницы """
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200
    assert 'Добро пожаловать!' in response.content.decode('utf-8')


@pytest.mark.django_db
def test_post_list_view(client, post, author):
    """  Тест для проверки списка постов """
    url = reverse('post_list')
    response = client.get(url)
    assert response.status_code == 200

    assert 'Тестовый пост' in response.content.decode('utf-8')
    assert author.name.encode() in response.content

