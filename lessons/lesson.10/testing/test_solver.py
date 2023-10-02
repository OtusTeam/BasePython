from unittest import TestCase

import pytest

from solver import Solver


class SolverTestCase(TestCase):
    def setUp(self) -> None:
        self.solver = Solver(2, 3)
        print("created solver", id(self.solver))

    def tearDown(self) -> None:
        print("dispose solver", id(self.solver))
        # self.user.delete()

    def test_add(self):
        res = self.solver.add()

        self.assertEqual(res, 5)
        # self.assertEqual(5, res)

    def test_mul(self):
        res = self.solver.mul()

        self.assertEqual(6, res)

    def test_many_add(self):
        for a, b, expected in [
            (2, 3, 5),
            (0, 0, 0),
            (0, 1, 1),
            (3, 2, 5),
        ]:
            with self.subTest(msg="test a + b", a=a, b=b, expected=expected):
                s = Solver(a, b)
                res = s.add()
                self.assertEqual(expected, res)

            # self.assertIs()
            # self.assertTrue()
            # self.assertIsInstance()
            # self.assertIsNotNone()
            # self.assertIsNone()
            # self.assertIn()
            # self.assertNotIn()
            # self.assertAlmostEqual(0.1 + 0.2, 0.3)
            # self.assertEqual(0.1 + 0.2, 0.3)


@pytest.fixture()
def solver():
    s = Solver(2, 3)
    return s


@pytest.fixture(
    params=[
        pytest.param((2, 3), id="first"),
        pytest.param((0, 0), id="zeros"),
        pytest.param((5, 3)),
        (5, 6),
    ]
)
def solver_multi(request):
    a, b = request.param
    solver = Solver(a, b)
    return solver


@pytest.fixture()
def solver_mix(request):
    a, b = request.param
    solver = Solver(a, b)
    return solver


# @pytest.fixture()
# def user_mix(request):
#     username = request.param
#     domain = fake.domain()
#     email = f"{username}@{domain}"
#     return User(
#         username=username,
#         email=email,
#         ...,
#     )


class TestSolver:
    def test_add(self, solver):
        res = solver.add()

        assert res == 5

    def test_mul(self, solver):
        res = solver.mul()

        assert res == 6

    def test_mul_many(self, solver_multi: Solver):
        res = solver_multi.mul()

        assert res == solver_multi.a * solver_multi.b

    def test_add_many(self, solver_multi: Solver):
        res = solver_multi.add()

        assert res == solver_multi.a + solver_multi.b

    # @pytest.mark.parametrize(["a", "b", "expected"], [
    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (2, 3, 5),
            pytest.param(0, 0, 0, id="zeros"),
            pytest.param(0, 1, 1, id="expected 1"),
            (3, 2, 5),
        ],
    )
    def test_many_add(self, a, b, expected):
        s = Solver(a, b)
        res = s.add()
        assert res == expected

    @pytest.mark.parametrize("solver_mix, expected", [
        pytest.param(("a", "b"), "ab"),
        pytest.param(("", ""), "", id="empty"),
        [("foo", "bar"), "foobar"],
    ], indirect=["solver_mix"])
    def test_add_strings(self, solver_mix: Solver, expected):
        res = solver_mix.add()
        assert res == expected


def test_data_equal():
    data1 = {
        "foo": "bar",
        "spam": "eggs",
    }

    data2 = {
        "foo": "bar",
        "fib": "baz",
        "spam": "eggs",
    }

    assert [1, ] == [1, ]
    assert [] is not []
    assert True
    assert data1 == data2, "expected same data on different runs"
    # assert False, "false should be true"

    # response = ...
    # status = ...
    #
    # assert response.status_code == status.HTTP_200_OK, response.text
