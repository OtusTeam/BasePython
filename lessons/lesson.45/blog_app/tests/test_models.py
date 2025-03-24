import pytest
from blog_app.models import Author, Post

# Для работы с реальной БД pytest --reuse-db
@pytest.mark.django_db
def test_author_creation(author):
    """ Проверка создания автора"""
    assert Author.objects.count() == 1
    assert author.name == 'Тестовый автор'
    assert str(author) == 'Тестовый автор'


@pytest.mark.django_db
def test_post_creation(post):
    """ Проверка создания поста"""
    assert Post.objects.count() == 1
    assert post.title == 'Тестовый пост'
    assert str(post) == 'Тестовый пост'
    assert post.rating == 5
    assert post.author.name == 'Тестовый автор'
    assert post.content == 'Содержание тестового поста'
