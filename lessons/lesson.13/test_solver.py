from pytest import mark, raises
from unittest import TestCase
from solver import Solver, mul, sub, SUB_ERROR_TEXT


@mark.parametrize(
    "values, expected_result",
    [
        ((3, 5), 15),
        ((1, 10), 10),
        ((1, 0), 0),
        # ((1, 0), 1),
        ((4, 8), 32),
    ]
)
def test_mul(values, expected_result):
    res = mul(*values)
    assert res == expected_result


def test_sub_raises():
    with raises(TypeError) as exc_info:
        sub(1, "")

    assert str(exc_info.value) == SUB_ERROR_TEXT


class TestSolver(TestCase):
    def test_add(self):
        res = Solver.add(1, 2)
        self.assertEqual(res, 3)

        res = Solver.add(4, 5)
        self.assertEqual(res, 9)

    def test(self):
        pass
