from unittest import TestCase

from pytest import fixture, raises

from solver import Solver, abc


class SolverTestCase(TestCase):

    def setUp(self) -> None:
        self.solver = Solver(2, 3)

    # def tearDown(self) -> None:

    def test_add(self):
        # s = Solver(2, 3)
        res = self.solver.add()
        self.assertEqual(5, res)

    def test_mul(self):
        # s = Solver(2, 3)
        res = self.solver.mul()
        self.assertEqual(6, res)


# class TestAbcTestCase(TestCase):
#
#     def test_abc(self):
#         res = abc()
#         self.assertEqual(123, res)


@fixture
def solver_inst():
    s = Solver(2, 3)
    print("created solver", s)
    return s


class TestSolver:
    def test_add(self, solver_inst):
        # s = Solver(2, 3)
        res = solver_inst.add()
        assert res == 5

    def test_mul(self, solver_inst):
        # s = Solver(2, 3)
        res = solver_inst.mul()
        assert res == 6

    def test_mul__raises(self, solver_inst):
        # solver_inst.b = str(solver_inst.b)
        solver_inst.b = None
        with raises(TypeError) as exc_info:
            solver_inst.mul()
        assert str(exc_info.value) == Solver.EXC_TYPE_ERROR_TEXT


def test_abc():
    res = abc()
    assert res == 123

