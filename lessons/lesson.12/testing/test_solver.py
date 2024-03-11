from unittest import TestCase

import pytest

from solver import Solver


class SolverTestCase(TestCase):
    assert_equal = TestCase.assertEqual

    def setUp(self):
        self.s = Solver(3, 4)

    def tearDown(self):
        # пример для работы с БД
        self.s.delete()

    def test_add(self):
        res = self.s.add()
        self.assert_equal(res, self.s.a + self.s.b)

    def test_add_multi(self):
        cases = [
            (1, 2, 3),
            (-1, 1, 0),
            (4, 5, 9),
            (3, 4, 7),
        ]
        for a, b, expected in cases:
            with self.subTest(
                msg=f"{a} + {b} = {expected}",
                a=a,
                b=b,
                expected=expected,
            ):
                solver = Solver(a, b)
                res = solver.add()
                self.assertEqual(expected, res)

    def test_mul(self):
        res = self.s.mul()
        self.assertEqual(self.s.a * self.s.b, res)

    def test_raises(self):
        self.s.a = "a"
        with self.assertRaises(TypeError) as exc_info:
            self.s.add()

        self.assertEqual(
            Solver.TYPE_ERROR_TEXT,
            str(exc_info.exception),
        )


def get_dataframe():
    return ...


@pytest.fixture()
def solver():
    # например создали пользователя в БД
    s = Solver(3, 4)
    # отдали на тесты
    yield s
    # вернулись после тестов
    # хороший тон: убери за собой
    s.delete()


@pytest.fixture(
    params=[
        pytest.param((3, 4), id="3*4=12"),
        pytest.param((5, 6), id="5*6=30"),
    ]
)
def solver_multi(request):
    a, b = request.param
    return Solver(a, b)


# todo: indirect init

class TestSolver:
    def test_add_single(self, solver):
        res = solver.add()
        assert res == solver.a + solver.b

    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (1, 2, 3),
            (-1, 1, 0),
            (0, 1, 1),
            (4, 5, 9),
            pytest.param(3, 4, 7, id="to-seven"),
        ],
    )
    def test_add(self, a, b, expected, solver):
        solver.a = a
        solver.b = b
        res = solver.add()
        assert res == expected

    def test_mul(self, solver_multi: Solver):
        assert solver_multi.mul() == solver_multi.a * solver_multi.b

    def test_raises(self, solver):
        solver.a = "a"
        with pytest.raises(TypeError, match=Solver.TYPE_ERROR_TEXT):
            solver.add()

        # with pytest.raises(TypeError) as exc_info:
        #     solver.add()
        #
        # assert str(exc_info.value) == Solver.TYPE_ERROR_TEXT


# @pytest.mark.parametrize()
def test_42():
    assert 42
