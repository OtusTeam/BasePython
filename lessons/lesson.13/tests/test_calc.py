import pytest
from src.calc import add, sub, mul, div, get_num


@pytest.mark.parametrize("num1, num2, result", [
    (1, 2, 3),
    (-1, 1, 0),
    (-1, -2, -3),
    (0, 0, 0),
])
def test_add(num1, num2, result):
    """Проверяем функцию сложения."""
    x = result
    assert add(num1, num2) == x


def test_sub(numbers_1, numbers_2):
    """Проверяем функцию вычитания."""
    assert sub(numbers_1[0], numbers_1[1]) == numbers_1[2]
    numbers_1[0] = 1000
    assert sub(numbers_2[0], numbers_2[1]) == numbers_2[2]
    numbers_2[0] = 50
    assert sub(0, 2) == -2


def test_mul(numbers_1, numbers_2):
    """Проверяем функцию умножения."""
    assert mul(numbers_1[0], numbers_1[1]) == 3000
    assert mul(numbers_2[0], numbers_2[1]) == -350


def test_div(capsys):
    """Проверяем функцию деления."""
    assert div(10, 2) == 5
    res = capsys.readouterr()
    assert res.out == "OK 123\n"
    # res.err

    # with pytest.raises(ValueError, match="Деление на ноль"):
    #     div(10, 0)


def test_get_num(mocker):
    mocker.patch('random.randint', return_value=7)
    result = get_num()
    assert result == 7