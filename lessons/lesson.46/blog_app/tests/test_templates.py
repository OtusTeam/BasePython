import pytest
from django.urls import reverse
from bs4 import BeautifulSoup

# from blog_app.models import Post, Author


@pytest.mark.django_db
def test_post_list_template(client, create_post_1, create_post_2, create_post_3):
    """Тест для проверки шаблона post_list.html"""
    url = reverse('post_list')
    response = client.get(url)
    assert response.status_code == 200

    soup = BeautifulSoup(response.content, 'html.parser')
    titles = [h5.get_text() for h5 in soup.find_all('h5')]
    assert len(titles) == 3
    assert titles[0] == 'Test post 1'
    assert titles == [create_post_1.title, create_post_2.title, create_post_3.title]