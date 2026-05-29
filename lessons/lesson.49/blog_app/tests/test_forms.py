import pytest

from blog_app.forms import PostForm, PostModelForm
from blog_app.models import Tag


@pytest.mark.django_db
def test_post_form_validation():
    """Проверка валидации PostForm"""
    form_data = {
        'title': 'Тестовый пост формы ',
        'content': 'Это содержимое формы тестового поста',
        'rating': 10
    }
    form = PostForm(data=form_data)
    assert form.is_valid()


@pytest.mark.django_db
def test_post_modelform_validation(author_1):
    """Проверка валидации PostModelForm"""
    tag = Tag.objects.create(name='Python')
    form_data = {
        'title': 'Тестовый пост ModelForm',
        'content': 'Это содержимое ModelForm тестового поста',
        'rating': 7,
        'author': author_1,
        'tags': [tag.id]
    }
    form = PostModelForm(data=form_data)
    assert form.is_valid()


@pytest.mark.django_db
def test_post_modelform_validation_negative_rating(author_1):
    """Проверка валидации PostModelForm"""
    tag = Tag.objects.create(name='Python')
    form_data = {
        'title': 'Тестовый пост ModelForm',
        'content': 'Это содержимое ModelForm тестового поста',
        'rating': 117,
        'author': author_1,
        'tags': [tag.id]
    }
    form = PostModelForm(data=form_data)
    assert not form.is_valid()


@pytest.mark.django_db
def test_post_modelform_validation_negative_title(author_1):
    """Проверка валидации PostModelForm"""
    tag = Tag.objects.create(name='Python')
    form_data = {
        'title': 'Тестовый пост казино ModelForm',
        'content': 'Это содержимое ModelForm тестового поста',
        'rating': 17,
        'author': author_1,
        'tags': [tag.id]
    }
    form = PostModelForm(data=form_data)
    assert not form.is_valid()
