import pytest
from blog_app.forms import PostForm, PostModelForm
from blog_app.models import Post, Author, Tag


@pytest.mark.django_db
def test_post_form_validation():
    """Проверка валидации PostForm."""
    form_data = {
        'title': 'Тестовый пост',
        'content': 'Это содержимое тестового поста',
        'rating': 10
    }
    form = PostForm(data=form_data)

    assert form.is_valid()


@pytest.mark.django_db
def test_post_modelform_validation(author_1):
    """Проверка валидации PostForm."""
    tag = Tag.objects.create(name='python')
    form_data = {
        'title': 'Тестовый пост',
        'content': 'Это содержимое тестового поста',
        'rating': 10,
        'author': author_1,
        'tags': [tag.id]
    }
    form = PostModelForm(data=form_data)

    assert form.is_valid()
    # assert True


@pytest.mark.django_db
def test_post_modelform_validation_negative(author_1):
    """Проверка валидации PostForm."""
    tag = Tag.objects.create(name='python')
    form_data = {
        'title': 'Тестовый пост',
        'content': 'Это содержимое тестового поста',
        'rating': 100,
        'author': author_1,
        'tags': [tag.id]
    }
    form = PostModelForm(data=form_data)

    assert not form.is_valid()