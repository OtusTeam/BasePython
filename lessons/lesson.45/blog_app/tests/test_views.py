import pytest
from django.urls import reverse


def test_index_view(client):
    """Тест для проверки корректности отображения главной страницы блога."""
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200
    assert 'Это главная страница вашего блога' in response.content.decode("utf-8")