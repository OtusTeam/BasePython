import pytest
from django.urls import reverse
from bs4 import BeautifulSoup


@pytest.mark.django_db
def test_post_list_template(client, post_1, post_2, post_3):
    """Тест для проверик шаблона списка постов."""
    url = reverse("post_list")
    response = client.get(url)
    assert response.status_code == 200

    soup = BeautifulSoup(response.content, "html.parser")
    titles = [h5.get_text() for h5 in soup.find_all("h5")]
    assert titles == [post_1.title, post_2.title, post_3.title]
