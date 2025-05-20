import pytest
from django.urls import reverse
# from blog_app.models import Author, Post
from bs4 import BeautifulSoup


@pytest.mark.django_db
def test_post_list_template_bs(client, author, post, post2):
    url = reverse('posts')
    response = client.get(url)
    assert response.status_code == 200

    soup = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')

    # titles = soup.find_all('h5')
    titles = [h5.get_text() for h5 in soup.find_all('h5')]
    assert len(titles) == 2
    assert 'Тестовый пост' in titles
    assert 'Новый пост 2' in titles