import re
from unittest import TestCase

import pytest

from solver import Solver


class SolverTestCase(TestCase):

    def setUp(self):
        self.solver = Solver(2, 3)

    def tearDown(self):
        self.solver.close()

    def test_mul(self):
        res = self.solver.mul()
        expected = self.solver.a * self.solver.b
        self.assertEqual(expected, res)
        self.solver.a = 1

    def test_one_add(self):
        res = self.solver.add()
        expected = self.solver.a + self.solver.b
        # self.assertEqual(res, 1)
        self.assertEqual(expected, res)

    def test_add(self):
        cases = [
            (1, 4, 5),
            (2, 3, 5),
            (0, 5, 5),
            (2, 5, 7),
            (2, 9, 11),
            (-5, 10, 5),
            (1, 2, 3),
        ]
        for a, b, expected in cases:
            with self.subTest(
                msg=f"{a} + {b} = {expected}",
                a=a,
                b=b,
                expected=expected,
            ):
                # b / a
                s = Solver(a, b)
                res = s.add()
                self.assertEqual(expected, res)


class SolverExceptionTestCase(TestCase):
    def setUp(self):
        self.solver = Solver("2", 3)

    def tearDown(self):
        self.solver.close()

    def test_add_raises_type_error_example_1(self):
        with self.assertRaises(TypeError) as exc_info:
            self.solver.add()

        # длинный путь. проверяем отдельно
        self.assertEqual(
            self.solver.INVALID_TYPE,
            exc_info.exception.args[0],
        )
        self.assertEqual(
            self.solver.a,
            exc_info.exception.args[1],
        )
        self.assertEqual(
            self.solver.b,
            exc_info.exception.args[2],
        )

        # короткий путь: проверяем всё сразу
        self.assertEqual(
            (self.solver.INVALID_TYPE, self.solver.a, self.solver.b),
            exc_info.exception.args,
        )

        # выберите что-то одно.

    def test_add_raises_type_error_example_2(self):
        with self.assertRaisesRegex(
            expected_exception=TypeError,
            expected_regex=re.escape(self.solver.INVALID_TYPE),
        ):
            self.solver.add()


@pytest.fixture()
def solver():
    s = Solver(2, 3)
    yield s
    s.close()


@pytest.fixture(
    params=[
        pytest.param((3, 4), id="3 and 4"),
        pytest.param((5, 6), id="5, 6"),
    ],
)
def solver_multi(request):
    a, b = request.param
    s = Solver(a, b)
    yield s
    s.close()


def test_create_solver():
    a = 2
    b = 3
    s = Solver(a, b)
    assert s.a == a
    assert s.b == b


class TestSolver:

    def test_one_add(self, solver):
        res = solver.add()
        expected = solver.a + solver.b
        assert res == expected

    def test_mul(self, solver):
        res = solver.mul()
        expected = solver.a * solver.b
        assert res == expected

    def test_add_raises_type_error(self):
        solver = Solver("2", 3)
        with pytest.raises(
            expected_exception=TypeError,
            match=re.escape(solver.INVALID_TYPE),
        ) as exc_info:
            solver.add()

        assert exc_info.value.args == (
            solver.INVALID_TYPE,
            solver.a,
            solver.b,
        )

    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (1, 4, 5),
            (2, 3, 5),
            pytest.param(0, 5, 5, id="zero a"),
            (2, 5, 7),
            (2, 9, 11),
            pytest.param(-5, 10, 5, id="negative a"),
            (1, 2, 3),
        ],
    )
    def test_add(self, a, b, expected):
        solver = Solver(a, b)
        expected = solver.a + solver.b
        res = solver.add()
        assert res == expected

    def test_add_new(self, solver_multi):
        res = solver_multi.add()
        expected = solver_multi.a + solver_multi.b
        assert res == expected
