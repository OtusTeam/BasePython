import pytest

from blog_app.models import Post, Author


@pytest.fixture
def create_author_1():
    """Фикстура для создания 1 автора."""
    return Author.objects.create(name='John')


@pytest.fixture
def create_author_2():
    """Фикстура для создания 2 автора."""
    return Author.objects.create(name='Bob')


@pytest.fixture
def create_post_1(create_author_1: Author):
    """Фикстура для создания поста 1."""
    return Post.objects.create(
        title='Test post 1',
        content='Test text 1',
        author=create_author_1,
        rating=7
    )


@pytest.fixture
def create_post_2(create_author_1: Author):
    """Фикстура для создания поста 1."""
    return Post.objects.create(
        title='Test post 2',
        content='Test text 2',
        author=create_author_1,
        rating=3
    )


@pytest.fixture
def create_post_3(create_author_2: Author):
    """Фикстура для создания поста 1."""
    return Post.objects.create(
        title='Test post 3',
        content='Test text 3',
        author=create_author_2,
        rating=5
    )