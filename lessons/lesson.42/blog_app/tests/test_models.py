import pytest
from blog_app.models import Author


@pytest.mark.django_db
def test_author_creation(author):
    assert Author.objects.count() == 1
    assert author.name == "Тестовый автор"
    assert str(author) == "Тестовый автор"
