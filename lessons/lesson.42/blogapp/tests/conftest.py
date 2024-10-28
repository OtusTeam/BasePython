import pytest

from blogapp.models import Post, Author


@pytest.fixture
def create_author():
    author = Author.objects.create(
        name='test_author',
        age=20,
        email='test@mail.ru',
        bio='test bio'
    )
    return author

