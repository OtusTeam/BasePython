import pytest
from blog_app.models import Author


@pytest.fixture
def author():
    return Author.objects.create(name="Тестовый автор")