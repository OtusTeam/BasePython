import pytest
from blog_app.models import Post, Author, Comment, Tag


@pytest.fixture(scope='function')
def author1():
    return Author.objects.create(name='Боб')


@pytest.fixture(scope='function')
def author2():
    return Author.objects.create(name='Мэри')


@pytest.fixture
def post1(author1):
    return Post.objects.create(
        title='Django пост',
        content='Вышла новая версия Django',
        rating=7,
        author=author1,
    )


@pytest.fixture
def post2(author1):
    return Post.objects.create(
        title='Python новость',
        content='Ускорение процессов python 3.15',
        rating=10,
        author=author1,
    )