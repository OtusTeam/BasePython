import pytest
from blog_app.models import Tag
from blog_app.forms import PostForm, PostModelForm


@pytest.mark.django_db
def test_post_form_valid():
    """Проверяем валидацию PostForm"""
    form_data = {
        'title': 'Тестовый пост',
        'content': 'Это содержание тестового поста',
        'rating': 10
    }
    form = PostForm(data=form_data)

    assert form.is_valid()

    clean_data = form.cleaned_data
    assert clean_data['title'] == form_data['title']




@pytest.mark.django_db
def test_postmodelform_valid(author_1):
    tag = Tag.objects.create(name='python')
    form_data = {
        'title': 'Тестовый пост',
        'content': 'Это содержание тестового поста',
        'rating': 10,
        'author': author_1,
        'tags': [tag.id],
    }

    form = PostModelForm(data=form_data)
    assert form.is_valid()


@pytest.mark.django_db
def test_postmodelform_valid_rating_negative(author_1):
    tag = Tag.objects.create(name='python')
    form_data = {
        'title': 'Тестовый пост',
        'content': 'Это содержание тестового поста',
        'rating': -5,
        'author': author_1,
        'tags': [tag.id],
    }

    form = PostModelForm(data=form_data)
    assert not form.is_valid()


@pytest.mark.django_db
def test_postmodelform_valid_title_negative(author_1):
    tag = Tag.objects.create(name='python')
    form_data = {
        'title': 'Тестовый пост крипта',
        'content': 'Это содержание тестового поста',
        'rating': 10,
        'author': author_1,
        'tags': [tag.id],
    }

    form = PostModelForm(data=form_data)
    assert not form.is_valid()
