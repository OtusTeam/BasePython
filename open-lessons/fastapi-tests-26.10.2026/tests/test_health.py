"""
A - Arrange
A - Act
A - Assert
"""
from starlette import status
from starlette.testclient import TestClient


def test_health(client: TestClient):
    # Arrange
    url = client.app.url_path_for("health")

    # Act
    response = client.get(url)

    # Assert
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"status": "ok"}
