import pytest
import os


@pytest.fixture(scope="session")
def numbers():
    """Фикстура возвращает тестовые данные."""
    yield [10, 7, 3]
    # os.remove("1.txt")