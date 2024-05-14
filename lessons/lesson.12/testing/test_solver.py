from unittest import TestCase

import pytest

from solver import Solver


class SolverTestCase(TestCase):

    def setUp(self):
        self.solver = Solver(2, 3)

    def tearDown(self):
        # print("clear solver:", self.solver.clear())
        self.solver.clear()

    def test_one_add(self):
        res = self.solver.add()
        expected = self.solver.a + self.solver.b
        self.assertEqual(expected, res)

    def test_add(self):
        cases = [
            (2, 3, 5),
            (3, 4, 7),
            (0, 0, 0),
            (1, 4, 5),
        ]
        for a, b, expected in cases:
            with self.subTest(
                msg=f"{a} + {b} = {expected}",
                a=a,
                b=b,
                expected=expected,
            ):
                s = Solver(a, b)
                res = s.add()
                self.assertEqual(expected, res)

    def test_mul(self):
        expected = self.solver.a * self.solver.b
        self.assertEqual(expected, self.solver.mul())

    def test_raises(self):
        self.solver.a = "a"
        with self.assertRaises(TypeError) as exc_info:
            self.solver.add()

        self.assertEqual(
            self.solver.TYPE_ERROR_TEXT,
            str(exc_info.exception),
        )


@pytest.fixture(scope="session")
def answer():
    # return random.randint(1, 100)
    return 42


def test_answer(answer):
    assert answer == 42


@pytest.fixture()
def solver(answer):
    # return Solver(answer, 3)
    s = Solver(answer, 3)
    yield s
    s.clear()


@pytest.fixture(
    params=[
        pytest.param((3, 4), id="3;4"),
        pytest.param((5, 6), id="5 and 6"),
    ],
)
def solver_multi(request):
    a, b = request.param
    # например, мы создали пользователя в базе данных
    s = Solver(a, b)
    # отдали пользователя в тесты
    yield s
    # после завершения теста (независимо от результата)
    # мы убираем за собой: удаляем пользователя из БД
    s.clear()


class TestSolver:

    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (2, 3, 5),
            pytest.param(3, 4, 7),
            pytest.param(0, 0, 0, id="zeros"),
            (1, 4, 5),
        ],
    )
    def test_add(self, a, b, expected):
        s = Solver(a, b)
        res = s.add()
        assert res == expected

    def test_one_add(self, solver: Solver):
        res = solver.add()
        assert res == solver.a + solver.b

    def test_mul(self, solver_multi: Solver):
        res = solver_multi.mul()
        assert res == solver_multi.a * solver_multi.b
