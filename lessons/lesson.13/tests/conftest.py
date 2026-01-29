import pytest
import os


@pytest.fixture(scope="session")
def numbers_1():
    """Фикстура возвращает тестовые данные."""
    return [10, 3, 7]


@pytest.fixture(scope="module")
def numbers_2():
    """Фикстура возвращает тестовые данные."""
    yield [-5, -7, 2]
    # os.remove('1.txt')
