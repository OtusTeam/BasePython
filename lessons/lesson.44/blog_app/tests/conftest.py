import pytest
from blog_app.models import Author, Post, Tag


@pytest.fixture
def author():
    return Author.objects.create(name='Тестовый автор')


@pytest.fixture
def post(author):
    return Post.objects.create(
        title="Тестовый пост",
        content="Содержание тестового поста",
        rating=10,
        author=author
    )


@pytest.fixture
def post2(author):
    return Post.objects.create(
        title="Тестовый пост2",
        content="Содержание тестового поста2",
        rating=10,
        author=author
    )


@pytest.fixture
def tag():
    return Tag.objects.create(
        name="Тестовый тэг",
    )