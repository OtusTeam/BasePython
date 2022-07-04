from unittest import TestCase

from pytest import fixture, mark, param, raises

from solver import Solver, div


# class TestSolver(TestCase):
class SolverTestCase(TestCase):

    def setUp(self) -> None:
        self.solver = Solver(2, 3)
        # print("prepared solver")

    def test_add(self):
        # s = Solver(2, 3)
        result = self.solver.add()
        # self.assertEqual(result, 5)
        self.assertEqual(5, result)
        # self.solver.a = 5

    def test_mul(self):
        # s = Solver(2, 3)
        result = self.solver.mul()
        self.assertEqual(6, result)


def test_div():
    result = div(10, 2)
    assert result == 5


@fixture
def solver_instance() -> Solver:
    a, b = 4, 5
    solver = Solver(a, b)
    return solver


@fixture
def solver_instance2(request) -> Solver:
    a, b = request.param
    solver = Solver(a, b)
    return solver


class TestSolver:

    def test_add(self, solver_instance):
        # s = Solver(4, 3)
        # s = solver_instance()
        result = solver_instance.add()
        assert result == 9

    @mark.parametrize("a, b, expected_result", [
        [3, 4, 12],
        (3, 2, 6),
        param(5, 7, 35),
        param(0, 7, 0, id="zero-mul"),
        param(0, 0, 0, id="zero-zero-mul"),
    ])
    # def test_mul(self, solver_instance):
    def test_mul(self, a, b, expected_result):
        s = Solver(a, b)
        # s = solver_instance()
        # res = solver_instance.mul()
        res = s.mul()
        assert res == expected_result

    @mark.parametrize("solver_instance2", [
        param(("a", "b")),
        param(("a", 1)),
    ], indirect=True)
    def test_mul__raises(self, solver_instance2: Solver):
        # s = Solver("a", 1)
        # s = Solver("a", "1")
        s = solver_instance2
        with raises(TypeError) as exc_info:
            s.mul()

        assert str(exc_info.value) == s.EXC_PARAMS_SHOULD_BE_NUMS
