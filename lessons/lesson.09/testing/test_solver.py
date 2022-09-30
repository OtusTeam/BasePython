from unittest import TestCase

import pytest
from pytest import fixture

from solver import Solver, div

# solver = Solver(2, 3)


class SolverTestCase(TestCase):

    # camelCase
    def setUp(self) -> None:
        self.solver = Solver(2, 3)

    # def tearDown(self) -> None:
    #     self.solver.dispose()

    # snake_case
    # Python -> snake
    def test_add(self):
        result = self.solver.add()
        self.assertEqual(5, result)
        self.solver.a = 4
        self.assertEqual(7, self.solver.add())
        # for params ...
        # self.assertEqual({"spam": "eggs"}, dict(spam='eggs'))
        # self.assertIsInstance()
        # self.assertTrue()
        # self.assertFalse()
        # self.assertIsNone()
        # self.asis
        # assert 5 == result

    def test_mul(self):
        result = self.solver.mul()
        self.assertEqual(6, result)


@fixture
def slvr():
    return Solver(2, 3)


@fixture
def solver_mix(request):
    a, b = request.param
    solver = Solver(a, b)
    return solver


class TestSolver:

    @pytest.mark.parametrize(
        "a, b, expected_result",
        [
            [1, 2, 3],
            [2, 2, 4],
            [0, 3, 3],
            [2, 1, 3],
            [3, 6, 9],
            ["3", "6", "36"],
        ],
    )
    def test_add(self, a: int | str, b: int | str, expected_result: int | str):
        # solver = solver_instance()
        # solver = Solver(2, 3)
        solver = Solver(a, b)
        assert solver.add() == expected_result

    @pytest.mark.parametrize("solver_mix, expected_result", [
        pytest.param([1, 2], 3, id="example-1"),
        pytest.param((5, 6), 11, id="demo-2"),
        pytest.param(("5", "6"), "56", id="demo-str"),
    ], indirect=["solver_mix"])
    def test_add_extra(self, solver_mix: Solver, expected_result):
        assert solver_mix.add() == expected_result

    def test_mul(self, slvr):
        # solver = solver_instance()
        # solver = Solver(2, 3)
        result = slvr.mul()
        assert result == 6

    def test_mul__raises(self):
        solver = Solver("a", "b")
        # solver = Solver("a", 3)
        with pytest.raises(TypeError) as exc_info:
            solver.mul()

        assert str(exc_info.value) == solver.PARAMS_TYPE_EXC_TEXT


def test_div():
    assert div(1, 2) == 0.5
