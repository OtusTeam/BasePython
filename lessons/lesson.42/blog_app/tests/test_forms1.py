import pytest
from django.urls import reverse
from blog_app.models import Author, Post


@pytest.mark.django_db
def test_post_create_view(mocker, client):
    # Создаем тестового автора
    author = Author.objects.create(name="Тестовый автор")

    # Мокаем метод save() на уровне экземпляра модели
    mock_save = mocker.patch('blog_app.models.Post.save', autospec=True)

    url = reverse('add_post_model')
    response = client.post(url, data={
        'title': 'Тестовый пост',
        'content': 'Тестовый контент',
        'rating': 5,
        'author': author.id
    })

    # Проверяем, что save() был вызван
    assert mock_save.call_count == 1, "Метод save() должен быть вызван один раз."

    # Проверяем, что запрос завершился редиректом
    assert response.status_code == 302, "Запрос должен завершиться перенаправлением."

    # Дополнительно можно проверить, что объект создан с правильными данными
    created_post = Post.objects.last()
    assert created_post.title == 'Тестовый пост'
    assert created_post.content == 'Тестовый контент'
    assert created_post.rating == 5
    assert created_post.author == author
