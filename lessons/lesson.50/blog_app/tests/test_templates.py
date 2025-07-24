import pytest
from django.urls import reverse
from bs4 import BeautifulSoup


@pytest.mark.django_db
def test_post_list_template(client, author, post, post2):
    url = reverse("post_list")
    response = client.get(url)

    assert response.status_code == 200

    soup = BeautifulSoup(response.content, "html.parser")


    assert soup.h3.text == "Тестовый пост"

    titles = [h3.get_text() for h3 in soup.find_all("h3")]

    assert "Тестовый пост" in titles
    assert "Тестовый пост2" in titles
    # assert "Тестовый пост3" in titles

    assert soup.find("h1", text="Список постов")
