from django.urls import reverse


def test_index_view(client):
    """Тесты для проверки главной страницы"""
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200
    assert "Добро пожаловать!" in response.content.decode()
    # assert b"Добро пожаловать!" in response.content
