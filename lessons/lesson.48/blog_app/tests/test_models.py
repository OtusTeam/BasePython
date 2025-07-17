import pytest
from blog_app.models import Post, Author

# Для работы с реальной базой данных pytest --reuse-db
@pytest.mark.django_db
def test_author_create(author):
    """ Проверка создания автора. """
    assert Author.objects.count() == 1
    assert author.name == "Тестовый автор"
    assert str(author) == "Тестовый автор"


@pytest.mark.django_db
def test_post_create(post):
    """ <UNK> <UNK> <UNK>. """
    assert Post.objects.count() == 1
    assert post.title == "Тестовый пост"
    assert str(post) == "Тестовый пост"
    assert post.rating == 10
