import pytest

from blog_app.forms import PostForm, PostModelForm
from blog_app.models import Post, Author, Tag


@pytest.mark.django_db
def test_post_form_valid():
    """Проверка валидации PostForm."""
    form_data = {
        "title": "Тестовый пост формы",
        "content": "Это содержание формы тестового поста",
        "rating": 10,
    }

    form = PostForm(data=form_data)
    assert form.is_valid()


@pytest.mark.django_db
def test_post_modelform_valid(author_1):
    """Проверка валидации PostModelForm."""
    tag = Tag.objects.create(name="Python")
    form_data = {
        "title": "Тестовый пост PostModelForm",
        "content": "Это содержание PostModelForm тестового поста",
        "rating": 7,
        "author": author_1,
        "tags": [tag.id],
    }

    form = PostModelForm(data=form_data)
    assert form.is_valid()


@pytest.mark.django_db
def test_post_modelform_negativ_content_valid(author_1):
    """Проверка валидации PostModelForm."""
    tag = Tag.objects.create(name="Python")
    form_data = {
        "title": "Тестовый пост PostModelForm",
        "content": "Это содержание крипта PostModelForm тестового поста",
        "rating": 7,
        "author": author_1,
        "tags": [tag.id],
    }

    form = PostModelForm(data=form_data)
    assert not form.is_valid()