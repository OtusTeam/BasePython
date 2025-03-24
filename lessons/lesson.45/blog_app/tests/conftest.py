import pytest
from blog_app.models import Author, Post


@pytest.fixture
def author():
    return Author.objects.create(name='Тестовый автор')


@pytest.fixture
def post(author):
    return Post.objects.create(title='Тестовый пост',
                               content="Содержание тестового поста",
                               rating=5,
                               author=author
                               )
