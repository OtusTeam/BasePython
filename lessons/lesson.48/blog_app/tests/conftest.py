import pytest

from blog_app.models import Author, Post


@pytest.fixture
def author_1():
    return Author.objects.create(name='John')


@pytest.fixture
def author_2():
    return Author.objects.create(name='Bob')


@pytest.fixture
def post_1(author_1):
    return Post.objects.create(
        author=author_1,
        title='Тестовый пост 1',
        content="Содержимое тестового поста 1",
        rating=5,
    )


@pytest.fixture
def post_2(author_1):
    return Post.objects.create(
        author=author_1,
        title='Тестовый пост 2',
        content="Содержимое тестового поста 2",
        rating=3,
    )


@pytest.fixture
def post_3(author_2):
    return Post.objects.create(
        author=author_2,
        title='Тестовый пост 3',
        content="Содержимое тестового поста 3",
        rating=7,
    )
