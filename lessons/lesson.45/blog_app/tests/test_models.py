import pytest
from blog_app.models import Post, Author


@pytest.mark.django_db
def test_author_creation(author_1, author_2):
    """Проверка создания объекта автора."""
    assert Author.objects.count() == 2
    assert author_1.name == 'John'
    assert author_2.name == 'Bob'
    assert str(author_2) == 'Bob!'


@pytest.mark.django_db
def test_post_creation(post_1, post_2, post_3):
    """Проверка создания объекта поста."""
    assert Post.objects.count() == 3
    assert post_1.title == 'Тестовый пост 1'
    assert post_2.rating == 10
    assert post_3.content == 'Содержание тестового поста 3'
    assert str(post_1) == 'Тестовый пост 1 - 7'