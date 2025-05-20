import pytest
from blog_app.models import Author, Post


@pytest.mark.django_db
def test_author_creation(author):
    assert Author.objects.count() == 1
    assert author.name == 'Тестовый автор'
    assert str(author) == 'Тестовый автор'


@pytest.mark.django_db
def test_post_creation(post):
    assert Post.objects.count() == 1
    assert post.title == 'Тестовый пост'
    assert post.author.name == 'Тестовый автор'
