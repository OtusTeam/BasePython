from unittest import TestCase

from pytest import fixture, mark, param

from solver import Solver


class SolverTestCase(TestCase):

    def setUp(self) -> None:
        self.solver = Solver(2, 3)

    # def tearDown(self) -> None:
    #     del self.solver

    # @classmethod
    # def setUpClass(cls) -> None:
    #     pass
    #
    # @classmethod
    # def tearDownClass(cls) -> None:
    #     pass

    # def test_add(self):
    #     for a, b in [(3, 5), (7, 2)]:
    #         solver = Solver(a, b)
    #         result = solver.add()
    #         self.assertEqual(result, 5)

    def test_add(self):
        result = self.solver.add()
        self.assertEqual(result, 5)

    def test_add_to_zero(self):
        self.solver.a = 0
        self.assertEqual(self.solver.add(), 3)

    def test_mul(self):
        result = self.solver.mul()
        self.assertEqual(result, 6)
        self.assertEqual(self.solver.b, 3)


@fixture()
def solver():
    return Solver(2, 3)


#
# @fixture(
#     params=[
#         (1, 2),
#         (3, 4),
#     ]
# )
# def solver_mix(request):
#     a, b = request.param
#     return Solver(a, b)


@fixture()
def solver_mix(request):
    a, b = request.param
    return Solver(a, b)


class TestSolver:

    def test_add(self, solver: Solver):
        res = solver.add()
        assert res == 5

    def test_add_zero(self, solver: Solver):
        solver.a = 0
        assert solver.add() == 3

    @mark.parametrize(
        "solver_mix, expected",
        [
            param((0, 1), 1, id="zero-plus-one"),
        ],
        indirect=["solver_mix"],
    )
    def test_add_zero_new(self, solver_mix: Solver, expected: int):
        assert solver_mix.add() == expected

    def test_mul(self, solver: Solver):
        res = solver.mul()
        assert res == 6

    @mark.parametrize(
        "a, b, expected",
        [
            (1, 2, 3),
            param(0, 0, 0, id="all-zeros"),
            param(0, 1, 1, id="zero-and-one"),
        ],
    )
    def test_add_many(self, a, b, expected):
        solver = Solver(a, b)
        result = solver.add()
        assert result == expected

    # def test_add_both_zeros...

    @mark.parametrize(
        "solver_mix, expected",
        [
            ((0, 0), 0),
            param([2, 3], 6),
            param([2, 5], 10, id="ten-expected"),
        ],
        indirect=["solver_mix"],
    )
    def test_mul_many(self, solver_mix: Solver, expected: int):
        result = solver_mix.mul()
        assert result == expected
