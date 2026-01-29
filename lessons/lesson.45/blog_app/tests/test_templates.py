import pytest
from bs4 import BeautifulSoup
from django.urls import reverse
from blog_app.models import Post, Author



@pytest.mark.django_db
def test_post_list_templates(client, author_1, author_2, post_1, post_2, post_3):
    url = reverse('post_list')
    response = client.get(url)
    assert response.status_code == 200

    assert 'Тестовый пост 1' in response.content.decode()
    assert 'Тестовый пост 2' in response.content.decode()
    assert 'Тестовый пост 3' in response.content.decode()


@pytest.mark.django_db
def test_post_list_templates_bs(client, author_1, author_2, post_1, post_2, post_3):
    url = reverse('post_list')
    response = client.get(url)
    assert response.status_code == 200

    soup = BeautifulSoup(response.content, 'html.parser')

    titles = [h5.get_text() for h5 in soup.find_all('h5')]
    assert 'Тестовый пост 1' in titles
    assert 'Тестовый пост 2' in titles
    assert 'Тестовый пост 3' in titles