import pytest
from main import add, div, sub, get_random_number, hello


@pytest.mark.parametrize('a, b, res', [
    (1, 2, 3),
    (5, 2, 7),
    (0, 2, 2),
    (-1, 2, 1),
    (-3, -2, -5),
])
def test_add(a, b, res):
    result = add(a, b)
    assert result == res


# def test_add1():
#     result = add(5, 2)
#     assert result == 7
#
#
# def test_add2():
#     result = add(0, 2)
#     assert result == 2
#
#
# def test_add3():
#     result = add(-1, 2)
#     assert result == 1
#
#
# def test_add_negative():
#     result = add(-3, -2)
#     assert result == -5


def test_div_by_zero(sample_number, sample_dict):
    sample_number[0] = 10
    try:
        div(sample_number, 0)
    except ValueError as e:
        assert str(e) == "Делить на ноль невозможно"


def test_div(sample_number):
    result = div(sample_number[0], 2)
    assert result == 3.5



def test_sub():
    result = sub(7, 4)
    assert result == 3


def test_get_random_number(mocker):
    mocker.patch("random.randint", return_value=15)
    result = get_random_number(1, 10)
    assert result == 15


def test_hello(capsys):
    hello()
    result = capsys.readouterr().out
    assert "Hello world" in result



if __name__ == '__main__':
    pytest.main(['-vv'])