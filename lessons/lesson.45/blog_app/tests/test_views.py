import pytest
from django.urls import reverse

from blog_app.models import Post


def test_index_view(client):
    """Тест для проверик главной страницы."""
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200
    assert "Добро пожаловать!" in response.content.decode()