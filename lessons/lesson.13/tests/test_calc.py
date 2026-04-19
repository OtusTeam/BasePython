import pytest
from src.calc import add, sub, mul, div, get_num


@pytest.fixture
def number1():
    """Фикстура возвращает тестовые данные."""
    return 10


@pytest.fixture
def number2():
    """Фикстура возвращает тестовые данные."""
    return 7


@pytest.fixture
def number3():
    """Фикстура возвращает тестовые данные."""
    return 3


@pytest.mark.parametrize("num1, num2, result", [
    (1, 3, 4),
    (-3, -2, -5),
    (-1, 4, 3),
    (5, 0, 5),
])
def test_add(num1, num2, result):
    """Проверяем функцию сложения с использованием parametrize."""
    assert add(num1, num2) == result


def test_sub(numbers):
    """Проверяем функцию вычитания."""
    x = numbers[0]
    y = numbers[1]
    z = numbers[2]
    assert sub(x, y) == z
    assert sub(3, 2) == 1
    assert sub(11, 4) == 7
    assert sub(5, 2) == 3
    numbers[0] = 1000


def test_mul(numbers):
    """Проверяем функцию умножения."""
    x = numbers[0]
    y = numbers[1]
    z = numbers[2]
    assert mul(x, y) == 7000
    assert mul(x, z) == 3000
    assert mul(11, 4) == 44
    assert mul(5, 2) == 10


def test_div():
    """Проверяем функцию деления."""
    assert div(10, 2) == 5

    # with pytest.raises(ZeroDivisionError):
    #     div(10, 0)

    with pytest.raises(ValueError, match="Деление на ноль"):
        div(10, 0)


def test_get_num(mocker):
    mocker.patch("random.randint", return_value=7)
    result = get_num()
    assert result == 107

# def test_add():
#     """Проверяем функцию сложения."""
#     assert add(1, 3) == 4
#     assert add(3, 2) == 5
#     assert add(1, 4) == 5
#     assert add(5, 2) == 7

#
# def test_add_2():
#     # assert add(1, 2) == 3
#     assert False