import pytest
from django.urls import reverse
from blog_app.models import Author, Tag
from blog_app.forms import PostModelForm

#
# @pytest.mark.django_db
# def test_post_form_valid():
#     bad_form_data = {
#         'title': 'Тестовый пост',
#         'content': 'Это  содержание',
#         'rating': 150
#     }
#     form1 = PostForm(bad_form_data)
#
#     assert not form1.is_valid()
#
#     form_data = {
#         'title': 'Тестовый пост',
#         'content': 'Это  содержание',
#         'rating': 10
#     }
#     form2 = PostForm(form_data)
#
#     assert form2.is_valid()
#
#     cleaned_data = form2.cleaned_data
#     assert cleaned_data['title'] == form_data['title']


@pytest.mark.django_db
def test_post_modelform_valid(client):
    author = Author.objects.create(name="Bob")
    tag = Tag.objects.create(name="django")
    form_data = {
        "title": "Coach be until пост",
        "content": "After themselves sea build baby spend make. Apply  содержание",
        "rating": 8,
        "author": author,
        "tags": [tag.id],
    }

    form = PostModelForm(form_data)
    # assert True
    assert form.is_valid()

    post = form.save()

    url = reverse("post_list")
    response = client.get(url)
    assert response.status_code == 200
    assert post.title.encode() in response.content
