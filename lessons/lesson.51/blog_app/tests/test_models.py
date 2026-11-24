import pytest

from blog_app.models import Author, Post


@pytest.mark.django_db
def test_create_author(create_author_1, create_author_2):
    """Тест создания автора."""
    assert Author.objects.count() == 2
    assert create_author_1.name == "John"
    assert create_author_2.name == "Bob"
    assert str(create_author_1) == "John !"


@pytest.mark.django_db
def test_create_post(create_post_1, create_post_2, create_post_3):
    """Тест создания поста."""
    assert Post.objects.count() == 3
    assert create_post_1.title == "Test post 1"
    assert create_post_2.content == "Test text 2"
    assert create_post_3.rating == 5
    assert str(create_post_1) == "Test post 1"
