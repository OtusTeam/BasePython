import pytest
from django.urls import reverse
from blog_app.models import Post


def test_index(client):
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200
    assert 'Это главная страница' in response.content.decode('utf-8')


@pytest.mark.django_db
def test_post_list(client, author, post):
    url = reverse('posts')
    response = client.get(url)

    assert response.status_code == 200

    assert post.title.encode() in response.content
    assert author.name.encode() in response.content


@pytest.mark.django_db
def test_post_filter(client, author, post):
    url = reverse('posts')
    response = client.get(url, {"rating": 7})
    assert response.status_code == 200

    assert post.title in response.content.decode('utf-8')

    low_rating_post = Post.objects.create(
        title='Низкий рейтинг',
        content='Тут низкий рейтинг',
        rating=2,
        author=author,
    )
    assert low_rating_post.title not in response.content.decode('utf-8')
