import pytest
from blog_app.models import Author, Post


@pytest.fixture
def author():
    return Author.objects.create(name='Тестовый автор')


@pytest.fixture
def post(author):
    return Post.objects.create(
        title='Тестовый пост',
        content='Содержимое тестового поста',
        rating=5,
        author=author,
    )


@pytest.fixture
def post2(author):
    return Post.objects.create(
        title='Новый пост 2',
        content='Содержимое нового поста 2',
        rating=7,
        author=author,
    )