import pytest

from blog_app.models import Post, Author


@pytest.mark.django_db
def test_create_author(author_1, author_2):
    """Проверяем создание объекта автора."""
    assert Author.objects.count() == 2
    assert author_1.name == "John"
    assert author_2.name == "Bob"
    assert str(author_2) == "Bob !"


@pytest.mark.django_db
def test_create_author(post_1, post_2, post_3):
    """Проверяем создание объекта поста."""
    assert Post.objects.count() == 3
    assert post_1.title == "Тестовый пост 1"
    assert post_2.rating == 3
    assert str(post_3) == "Пост - Тестовый пост 3"