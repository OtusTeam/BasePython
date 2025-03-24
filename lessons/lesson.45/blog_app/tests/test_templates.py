import pytest
from django.urls import reverse
from blog_app.models import Post, Author
from bs4 import BeautifulSoup


@pytest.mark.django_db
def test_post_list_view(client, author, post):
    """  Тест для проверки списка постов """
    Post.objects.create(title='Тестовый пост 2',
                        content="Содержание тестового поста 2",
                        rating=3,
                        author=author
                        )


    url = reverse('post_list')
    response = client.get(url)
    assert response.status_code == 200

    assert 'Тестовый пост 2' in response.content.decode('utf-8')
    assert 'Тестовый пост' in response.content.decode('utf-8')



@pytest.mark.django_db
def test_post_list_view_bs(client, author, post):
    """  Тест для проверки списка постов c помощью bs"""
    Post.objects.create(title='Тестовый пост 2',
                        content="Содержание тестового поста 2",
                        rating=3,
                        author=author
                        )


    url = reverse('post_list')
    response = client.get(url)
    assert response.status_code == 200

    soup = BeautifulSoup(response.content, 'html.parser')
    assert soup.h5.text == 'Тестовый пост'
    assert soup.p.text == 'Содержание тестового поста'

    assert soup.find('title').text == ' Список постов '
    # soup1 = soup.find_all('h5')