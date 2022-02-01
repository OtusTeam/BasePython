from os import getenv
from pytest import fixture, exit

from app import app

if getenv("CONFIG") != "TestingConfig":
    exit("not in testing env")


@fixture
def client():
    with app.test_client() as test_client:
        with app.app_context():
            yield test_client
