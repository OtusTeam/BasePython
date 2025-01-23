import pytest


@pytest.fixture(scope='session')
def data():

    yield [1, 2, 3]
    print('clean up')