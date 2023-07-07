from unittest import TestCase

from pytest import fixture, mark, param

from solver import Solver


pytestmark = mark.solver


class SolverTestCase(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        pass
        # cls.db = Database(...)

    @classmethod
    def tearDownClass(cls) -> None:
        pass
        # cls.db.close()

    def setUp(self) -> None:
        # self.user = User(...)
        # self.db.add(self.user)
        # self.db.commit()
        self.solver = Solver(2, 3)

    def tearDown(self) -> None:
        print("delete solver", self.solver)
        # self.db.delete(self.user)

    def test_add(self):
        # self.user.username = ".."
        s = self.solver
        result = s.add()
        self.assertEqual(result, 5)
        s.a = 4
        result = s.add()
        self.assertEqual(result, 7)
        s.a = 0
        s.b = 0
        result = s.add()
        self.assertEqual(result, 0)

        # for i in range(...):

    def test_mul(self):
        # self.user.age = 42
        # self.user.add_friend(...)

        result = self.solver.mul()
        self.assertEqual(result, 6)


@fixture(scope="function")
def solver():
    # return Solver(2, 3)
    solver = Solver(2, 3)
    return solver


@fixture(params=[
    param((2, 3), id="first"),
    param((0, 0), id="zero"),
    param((4, 5)),
])
def solver_multi(request):
    a, b = request.param
    solver = Solver(a, b)
    return solver


@fixture()
def solver_mix(request):
    a, b = request.param
    solver = Solver(a, b)
    return solver


# def solver_mix()


class TestSolver:
    @mark.parametrize("new_a", [
        param(3,),
        param(5,),
    ])
    @mark.parametrize("new_b", [
        param(8,),
        param(2,),
    ])
    def test_add(self, solver_multi: Solver, new_a: int, new_b: int):
        result = solver_multi.add()
        assert result == solver_multi.a + solver_multi.b
        solver_multi.a = new_a
        result = solver_multi.add()
        assert result == new_a + solver_multi.b
        solver_multi.b = new_b
        result = solver_multi.add()
        assert result == new_a + new_b

    def test_mul_one(self, solver: Solver):
        result = solver.mul()
        assert result == 6

    @mark.parametrize("a, b, expected", [
        (2, 3, 6),
        (3, 0, 0),
        param(5, 5, 25, id="5^2"),
        param(0, 0, 0, id="zeros"),
    ])
    def test_mul(self, a, b, expected):
        solver = Solver(a=a, b=b)
        result = solver.mul()
        assert result == expected

    @mark.parametrize("solver_mix, expected", [
        param((3, 4), 12, id="twelve"),
        param((4, 4), 16, id="hex"),
        param((4, 0), 0),
        param((0, 3), 0),
    ], indirect=["solver_mix"])
    def test_mul_mix(self, solver_mix: Solver, expected: int):
        result = solver_mix.mul()
        assert result == expected
