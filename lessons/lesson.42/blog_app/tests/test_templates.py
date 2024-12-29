import pytest
from django.urls import reverse
from blog_app.models import Author

# Create your tests here.
@pytest.mark.django_db
def test_author_list(client):
    author = Author.objects.create(name="Тестовый автор")
    url = reverse('author_list')
    response = client.get(url)
    assert response.status_code == 200

