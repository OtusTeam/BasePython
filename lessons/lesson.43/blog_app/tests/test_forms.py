import pytest
from blog_app.forms import PostForm
from blog_app.models import Author


@pytest.mark.django_db
def test_post_form():
    form_data = {
        'title': 'Тестовый поcт',
        'content': 'Тестовый контент',
        'rating': 5,
        'author': Author.objects.create(name="Тестовый автор")
    }

    form = PostForm(data=form_data)
    assert form.is_valid()

    cleaned_data = form.cleaned_data
    assert cleaned_data['title'] == form_data['title']
    assert cleaned_data['content'] == form_data['content']
    assert cleaned_data['rating'] == form_data['rating']
    assert cleaned_data['author'] == form_data['author']