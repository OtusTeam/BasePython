from unittest import TestCase

from pytest import fixture, mark, param, raises

from solver import Solver


class SolverTestCase(TestCase):

    def setUp(self) -> None:
        self.solver = Solver(2, 3)
        print("prepared solver")

    def test_add(self):
        # s = Solver(2, 3)
        res = self.solver.add()
        # self.solver.a = 5
        self.assertEqual(5, res)

    def test_mul(self):
        # s = Solver(2, 3)
        res = self.solver.mul()
        self.assertEqual(6, res)


@fixture
def solver_inst():
    solver = Solver(4, 5)
    return solver


@fixture
def solver_inst2(request) -> Solver:
    a, b = request.param
    solver = Solver(a, b)
    return solver


class TestSolver:
    def test_add(self, solver_inst):
        # s = solver_inst()
        res = solver_inst.add()
        assert res == 9

    @mark.parametrize(
        "solver_inst2, expected_result",
        [
            [(3, 4), 12],
            param((5, 6), 30),
            param((0, 0), 0, id="zeros"),
            param(("123", 2), "123123", id="string-mul"),
        ],
        indirect=["solver_inst2"],
    )
    def test_mul(self, solver_inst2: Solver, expected_result):
        # s = Solver(1, 2)
        # assert s.mul() == 2
        # s = Solver(3, 4)
        # assert s.mul() == 12
        # s = Solver(5, 6)
        # assert s.mul() == 30
        # s = Solver()

        res = solver_inst2.mul()
        assert res == expected_result

    @mark.parametrize(
        "solver_inst2",
        [
            param(("a", "b")),
            # param(("a", None)),
            # param((0, 0), 0, id="zeros"),
            # param(("123", 2), "123123", id="string-mul"),
        ],
        indirect=True,
    )
    def test_mul__raises(self, solver_inst2: Solver):
        s = solver_inst2

        with raises(TypeError) as exc_info:
            s.mul()
        assert str(exc_info.value) == s.EXC_TYPE_ERROR_TEXT

        # print(exc_info.value)
        # NEVER!!!!
        # try:
        #     s.mul()
        # except TypeError:
        #     print("ok")
        # else:
        #     assert False, "expected raise TypeError"
