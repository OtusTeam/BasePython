import pytest
from blog_app.forms import PostForm, PostModelForm
from blog_app.models import Author, Post


@pytest.mark.django_db
def test_post_form_valid(author):
    form_data = {
        'title': 'Test form',
        'content': 'content form',
        'author': author,
        'rating': 3,
    }

    form = PostForm(data=form_data)
    assert form.is_valid()

    cleaned_data = form.cleaned_data
    assert cleaned_data['title'] == form_data['title']


@pytest.mark.django_db
def test_post_model_form_title(author):
    form_data = {
        'title': 'Test',
        'content': 'content form',
        'author': author,
        'rating': 3,
    }

    form = PostModelForm(data=form_data)
    assert not form.is_valid()


@pytest.mark.django_db
def test_post_model_form_content(author):
    form_data = {
        'title': 'Test form',
        'content': 'казино 1xbet',
        'author': author,
        'rating': 3,
    }

    form = PostModelForm(data=form_data)
    assert not form.is_valid()