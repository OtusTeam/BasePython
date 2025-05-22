import pytest


@pytest.fixture(scope="function")
def sample_number():
    data =  [7, 2, 3]
    print(data)
    yield data
    data.clear()
    print(data)


@pytest.fixture
def sample_dict():
    return [7, 2, 3]


@pytest.fixture
def sample_list():
    return [7, 2, 3]