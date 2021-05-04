from pathlib import Path
from time import sleep

import docker
import requests
import pytest
from faker import Faker


current_file = Path(__file__).resolve()
folder_test_homework_0X = current_file.parent
homework_0X = folder_test_homework_0X.name.replace("test_", "")
homework_0X_path = folder_test_homework_0X.parent.parent / homework_0X
dockerfile_path = homework_0X_path / "Dockerfile"

if not (dockerfile_path.is_file() and len(dockerfile_path.read_text().splitlines()) > 5):
    pytestmark = pytest.mark.skip("Dockerfile is not ready")


fake = Faker()


PORT = 8000
LOCAL_PORT = 12345


@pytest.fixture
def docker_client():
    return docker.from_env()


@pytest.fixture
def image_name():
    tag = f"homework-image-{fake.word()}:latest"
    print(f"name for image: {repr(tag)}")
    return tag


@pytest.fixture
def build_image(docker_client):
    build_path = str(homework_0X_path)
    print("Building in", build_path)
    image_object, build_logs = docker_client.images.build(
        path=build_path,
        # dockerfile=str(dockerfile_path),
        # tag=image_name,
    )
    yield image_object
    # print logs?


@pytest.fixture
def run_image(docker_client, build_image):
    from docker.models.containers import Container
    container: Container = docker_client.containers.run(build_image, detach=True, ports={PORT: LOCAL_PORT})
    print("running docker container detached")
    # give some time to for the web app to start
    sleep(1)
    yield container
    print("stopping docker container")
    container.stop()
    print("docker container stopped")


def test_build_and_run_app(run_image):
    print("sending request to the image")
    resp: requests.Response = requests.get(f"http://localhost:{LOCAL_PORT}/ping/")
    assert resp.status_code == 200
    assert resp.json() == {"message": "pong"}
