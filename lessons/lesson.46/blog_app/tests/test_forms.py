import pytest

from blog_app.forms import PostForm, PostModelForm
from blog_app.models import Post, Author, Tag, Comment


@pytest.mark.django_db
def test_post_form_valid():
    """Проверка валидности формы создания поста."""
    form_data = {
        'title': 'Test post 5',
        'content': 'Test text 5',
        'rating': 2
    }
    form = PostForm(data=form_data)
    assert form.is_valid()

    assert form.cleaned_data['title'] == 'Test post 5'
    assert form.cleaned_data['content'] == 'Test text 5'
    assert form.cleaned_data['rating'] == 2


@pytest.mark.django_db
def test_post_form_not_valid():
    """Проверка не валидности формы ."""
    form_data = {
        'title': 'Test post 5',
        'content': 'Test text 5',
        'rating': 12
    }
    form = PostForm(data=form_data)
    assert not form.is_valid()


@pytest.mark.django_db
def test_post_modelform_valid(create_author_1):
    """Проверка валидности PostModelForm."""
    tag = Tag.objects.create(name='python')
    form_data = {
        'title': 'Test post ModelForm',
        'content': 'Это содердание PostModelForm тестового поста',
        'rating': 7,
        'author': create_author_1,
        'tags': [tag]
    }
    form = PostModelForm(data=form_data)
    assert form.is_valid()
    # assert True


@pytest.mark.django_db
def test_post_modelform_negativ_content_valid(create_author_1):
    """Проверка валидности PostModelForm."""
    tag = Tag.objects.create(name='python')
    form_data = {
        'title': 'Test post ModelForm',
        'content': 'Это содержание крипта PostModelForm тестового поста',
        'rating': 7,
        'author': create_author_1,
        'tags': [tag]
    }
    form = PostModelForm(data=form_data)
    assert not form.is_valid()
    # assert True