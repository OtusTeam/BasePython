import pytest
from blog_app.models import Post, Author, Comment


@pytest.mark.django_db
def test_author_create(author_1, author_2):
    assert Author.objects.count() == 2
    assert author_1.name == 'Боб'
    assert author_2.name == 'Мэри'
    assert str(author_1) == 'Боб!'


@pytest.mark.django_db
def test_post_create(post_1, post_2, post_3):
    assert Post.objects.count() == 3
    assert post_1.content == 'Содержание тестового поста 1'
    assert post_2.rating == 2
    assert post_1.author.name == 'Боб'
    assert str(post_3) == 'Тестовый пост 3'