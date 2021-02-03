from unittest import TestCase

from pytest import mark

from solver import Solver, mul


@mark.parametrize("values, expected", [
    ((2, 3), 6),
    ((3, 3), 9),
    ((1, 0), 0),
    # User(joined_at="00:00:00T21.03.2010")
])
def test_mul(values, expected):
    print("processing values", values, "expected", expected)
    res = mul(*values)
    # res = values[0] * values[1]
    assert res == expected


def test_some_test(my_fixture):
    print("my_fixture", my_fixture)


class TestSolver(TestCase):
    def test_add(self):
        solver = Solver()
        # res = Solver.add(2, 3)
        res = solver.add(2, 3)
        self.assertEqual(res, 5)

        res = solver.add(1, 5)
        self.assertEqual(res, 6)

        res = solver.add(1, 4)
        self.assertEqual(res, 5)

        res = solver.add(0, 5)
        self.assertEqual(res, 5)

