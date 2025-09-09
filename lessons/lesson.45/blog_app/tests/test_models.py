import pytest
from blog_app.models import Author, Post


@pytest.mark.django_db
def test_author_creation(author1, author2):
    assert Author.objects.count() == 2
    assert author1.name == 'Боб'
    assert author2.name == 'Мэри'
    assert str(author1) == 'Боб!'


@pytest.mark.django_db
def test_post_creation(post1):
    assert Post.objects.count() == 1
    assert post1.title == 'Django пост'
    assert post1.content == 'Вышла новая версия Django'
    assert post1.rating == 7
    assert post1.author.name == 'Боб'
    assert str(post1) == 'Пост - Django пост'


