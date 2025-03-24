import pytest
from blog_app.models import Author, Post, Tag
from blog_app.forms import PostForm, PostModelForm
from blog_app.tests.conftest import author


@pytest.mark.django_db
def test_post_modelform_validation():
    """  Проверка валидации модельной формы """
    author = Author.objects.create(name='Тестовый автор')
    tag = Tag.objects.create(name='Тестовый тег')
    form_data = {
        'title': 'Модельный пост',
        'content': 'Содержание модельного поста',
        'author': author.id,
        'tags': [tag.id],
        'rating': 5
    }

    form = PostModelForm(data=form_data)

    assert form.is_valid()

    post = form.save()

    assert post.title == form_data['title']
