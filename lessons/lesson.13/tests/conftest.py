import pytest
import os


@pytest.fixture(scope="function")
def numbers():
    yield [27, 7, 20]
    # os.remove("1.txt")