import pytest
from blog_app.forms import PostForm, PostModelForm
from blog_app.models import Author, Post, Tag


@pytest.mark.django_db
def test_post_form_valid():
    form_data = {
        "title": "Заголовок",
        "content": "Содержимое",
        "rating": 7
    }
    form = PostForm(data=form_data)

    assert form.is_valid()

    cleaned_data = form.cleaned_data
    assert cleaned_data['title'] == form_data['title']
    assert cleaned_data['rating'] == form_data['rating']


@pytest.mark.django_db
def test_post_modelform_valid(author, tag):

    form_data = {
        "title": "Заг",
        "content": "Содержимое",
        "rating": 7,
        "tags": [tag.pk],
        "author": author.pk,
    }
    form = PostModelForm(data=form_data)

    assert not form.is_valid()

    # cleaned_data = form.cleaned_data
    # assert cleaned_data['title'] == form_data['title']
    # assert cleaned_data['rating'] == form_data['rating']