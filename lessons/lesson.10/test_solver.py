from unittest import TestCase

import pytest

from solver import Solver, add


@pytest.fixture
def solver_inst():
    return Solver(4, 7)


class TestSolverTestCase(TestCase):

    def test_add(self):
        s = Solver(2, 3)
        result = s.add()
        self.assertEqual(5, result)

    def test_mul(self):
        s = Solver(4, 5)
        result = s.mul()
        self.assertEqual(20, result)


def test_add():
    res = add(1, 2)
    assert res == 3


class TestSolver:
    def test_add(self, solver_inst):
        result = solver_inst.add()
        assert result == solver_inst.a + solver_inst.b

    def test_mul__raises_typeerror(self, solver_inst):
        solver_inst.b = str(solver_inst.b)
        with pytest.raises(TypeError) as exc_info:
            solver_inst.mul()
        assert str(exc_info.value) == Solver.EXC_TYPE_ERROR_TEXT
