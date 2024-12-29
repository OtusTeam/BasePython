import pytest
from django.urls import reverse
from blog_app.models import Author, Post


@pytest.mark.django_db
def test_post_create_view(mocker, client):
    author = Author.objects.create(name="Тестовый автор")
    mocker_create = mocker.patch('blog_app.models.Post.objects.save')

    # mocker_create.return_value = Post(
    #     id=1,
    #     title='Тестовый пост',
    #     content='Тестовый контент',
    #     rating=5,
    #     author=author
    # )

    url = reverse('add_post_model')
    response = client.post(url, data={
        'title': 'Тестовый пост',
        'content': 'Тестовый контент',
        'rating': 5,
        'author': author.id
    })

    assert mocker_create.call_count == 1


    # mocker_create.assert_called_once_with(
    #     title='Тестовый пост',
    #     content='Тестовый контент',
    #     rating=5,
    #     author=Author.objects.create(name="Тестовый автор")
    # )

    # assert True

# Create your tests here.
# @pytest.mark.django_db
# def test_index(client):
#     url = reverse('index')
#     response = client.get(url)
#     assert response.status_code == 200
#     # print(response.content.decode()) # response
#     assert "Добро пожаловать!" in response.content.decode()
#
#
# if __name__ == '__main__':
#     pytest.main()


