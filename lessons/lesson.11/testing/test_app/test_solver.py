from unittest import TestCase
from pytest import mark, param, raises

from app.solver import Solver, mul, UNEXPECTED_TYPE


class TestSolver(TestCase):

    def test_add(self):
        solver = Solver()

        result = solver.add(2, 3)
        self.assertEqual(result, 5)

    def test_add2(self):
        solver = Solver()

        result = solver.add(2, 4)
        self.assertEqual(result, 6)

    def test_add_type_error(self):
        solver = Solver()

        with self.assertRaises(TypeError) as exc_info:
            solver.add('2', 4)
            # solver.add(2, 4)

        self.assertEqual(str(exc_info.exception), UNEXPECTED_TYPE)


class TestSolver2:
    def test_add_type_error(self):
        solver = Solver()

        with raises(TypeError) as exc_info:
            solver.add('2', 4)

        assert str(exc_info.value) == UNEXPECTED_TYPE


@mark.parametrize("values, expected", [
    ((2, 3), 6),
    ((5, 3), 15),
    ((7, -1), -7),
    param((6, 9), 54, id="test 6 * 9")
])
def test_mul(values, expected):
    result = mul(*values)
    assert result == expected
