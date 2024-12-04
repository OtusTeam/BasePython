import pytest


@pytest.fixture(scope="class")
def data():
    return [1, 2, 3, 4, 5]


@pytest.fixture(scope='module')
def sample_data():
    print('\nСоздаю список\n')
    # print(data_1)
    data_1 = [1, 2, 3, 4, 5]
    yield data_1
    print('\nОчищаю список\n')
    data_1.clear()
    print(data_1)

