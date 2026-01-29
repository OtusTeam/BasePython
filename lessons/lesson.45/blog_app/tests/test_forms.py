import pytest
from blog_app.forms import PostForm, PostModelForm
from blog_app.models import Post, Author, Tag


@pytest.mark.django_db
def test_post_form_validation():
    form_data = {
        'title': 'Тестовый пост формы',
        'content': 'Содержание тестового поста формы',
        'rating': 11,
    }
    form = PostForm(data=form_data)

    assert form.is_valid()
    cleaned_data = form.cleaned_data
    assert cleaned_data['title'] == form_data['title']
    assert cleaned_data['content'] == form_data['content']
    assert cleaned_data['rating'] == form_data['rating']


@pytest.mark.django_db
def test_post_modelform_validation(author_1):
    tag = Tag.objects.create(name='python')
    form_data = {
        'title': 'Тестовый пост моделформы',
        'content': 'Содержание тестового поста моделформы',
        'rating': 17,
        'author': author_1,
        'tag': [tag.id],
    }
    form = PostModelForm(data=form_data)

    assert form.is_valid()


@pytest.mark.django_db
def test_post_modelform_valid_rating_negative(author_1):
    tag = Tag.objects.create(name='python')
    form_data = {
        'title': 'Тестовый пост моделформы',
        'content': 'Содержание тестового поста моделформы',
        'rating': -17,
        'author': author_1,
        'tag': [tag.id],
    }
    form = PostModelForm(data=form_data)

    assert not form.is_valid()


@pytest.mark.django_db
def test_post_modelform_valid_title_negative(author_1):
    tag = Tag.objects.create(name='python')
    form_data = {
        'title': 'Тестовый пост крипта моделформы',
        'content': 'Содержание тестового поста моделформы',
        'rating': 7,
        'author': author_1,
        'tag': [tag.id],
    }
    form = PostModelForm(data=form_data)

    assert not form.is_valid()
