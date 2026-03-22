import pytest
from blog_app.models import Post, Author


@pytest.fixture
def author_1():
    return Author.objects.create(name="John")


@pytest.fixture
def author_2():
    return Author.objects.create(name="Bob")


@pytest.fixture
def post_1(author_1):
    return Post.objects.create(
        title="Тестовый пост 1",
        content="Содержание тестового поста 1",
        rating=7,
        author=author_1
    )


@pytest.fixture
def post_2(author_1):
    return Post.objects.create(
        title="Тестовый пост 2",
        content="Содержание тестового поста 2",
        rating=10,
        author=author_1
    )


@pytest.fixture
def post_3(author_2):
    return Post.objects.create(
        title="Тестовый пост 3",
        content="Содержание тестового поста 3",
        rating=5,
        author=author_2
    )
