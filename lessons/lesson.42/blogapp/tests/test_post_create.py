import pytest
from blogapp.models import Post, Author
from django.urls import reverse

from blogapp.tests.conftest import create_author


@pytest.mark.django_db
@pytest.mark.parametrize('title, content, category, is_published, published_date', [
    ('test_title', 'test_content', 'test_category', True, '2022-01-01'),
    ('test_title2', 'test_content2', 'test_category2', True, '2022-01-11'),])
def test_post_create(client, create_author, title, content, category, is_published, published_date):

    post_data = {
        'title': title,
        'content': content,
        'author': create_author.id,
        'category': category,
        'is_published': is_published,
        'published_date': published_date,
    }

    response = client.post(reverse('post_create'), data=post_data)

    assert response.status_code == 302
    post = Post.objects.last()

    assert post.title == title
    assert post.content == content
    assert post.category == category
    assert post.is_published == is_published
    # assert post.published_date == published_date


    # post = Post.objects.create(
    #     title='test_title',
    #     content='test_content',
    #     author=author,
    #     category='test_category',
    #     is_published=True,
    #     published_date='2022-01-01'
    # )
