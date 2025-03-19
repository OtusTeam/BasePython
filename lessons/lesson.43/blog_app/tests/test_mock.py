import pytest
from blog_app.models import Author, Post


@pytest.mark.django_db
def test_post_list_view(mocker, post, author):
    """  Тест для проверки списка постов """

    mocker_str = mocker.patch.object(Post, '__str__', return_value='Мокковый пост')

    assert str(post) == 'Мокковый пост'