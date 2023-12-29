from unittest import TestCase

import pytest

from solver import Solver


class SolverTestCase(TestCase):
    def setUp(self) -> None:
        self.solver = Solver(5, 3)
        print("created solver", id(self.solver))

    def tearDown(self) -> None:
        print("dispose solver", id(self.solver))
        # solver.close()
        # solver.dispose()

    def test_add(self):
        res = self.solver.add()
        # expected_res = 5
        expected_res = self.solver.a + self.solver.b
        # self.assertEqual(res, expected_res)
        self.assertEqual(expected_res, res)

    def test_mul(self):
        s = self.solver
        res = s.mul()
        # expected_res = 6
        expected_res = s.a * s.b
        self.assertEqual(expected_res, res)

    def test_add_multi(self):
        for a, b, expected in [
            (2, 3, 5),
            # ("2", 3, None),
            (0, 0, 0),
            (0, 1, 1),
            ("abc", "qwe", "abcqwe"),
        ]:
            with self.subTest(
                msg="test a + b",
                a=a,
                b=b,
                expected=expected,
            ):
                s = Solver(a, b)
                res = s.add()
                self.assertEqual(expected, res)

            # self.assertIn()
            # self.assertIs()
            # self.assertIsNot()
            # self.assertIsNone()
            # self.assertIsNotNone()
            # self.assertTrue()
            # self.assertFalse()
            # self.assertAlmostEqual(0.1 + 0.2, 0.3)
            # self.assertIsInstance()
            # self.assertTrue(isinstance("abc", str))
            # self.assertIsInstance("abc", str)
            #
            # assert "a" in "foobar"
            # assert isinstance("a", str)

    def test_add_invalid_params(self):
        s = Solver("a", 1)
        with self.assertRaises(TypeError):
            s.add()


@pytest.fixture(scope="session")
def conn():
    conn = create_db_connection(...)
    yield conn
    conn.dispose()


@pytest.fixture()
def db(conn):
    # [1, 2] == [1, 2]
    # a         b
    # is None

    db = create_db(conn)
    yield db
    db.close()


@pytest.fixture()
def user(db):
    user = User(username=...)
    db.add(user)
    user.save()
    yield user
    db.delete(user)


@pytest.fixture()
def solver():
    solver = Solver(2, 3)
    print("[pt] created solver", id(solver))
    yield solver
    # return solver
    print("dispose solver", id(solver))


class TestSolver:
    def test_add(self, solver):
        res = solver.add()
        expected = solver.a + solver.b
        assert res == expected

    def test_mul(self, solver):
        s = solver
        res = s.mul()
        expected = s.a * s.b
        assert res == expected

    # @pytest.mark.parametrize(["a", "b", "expected"])
    @pytest.mark.parametrize("a, b, expected", [
        (1, 2, 3),
        (3, 2, 5),
        pytest.param(0, 0, 0, id="zeros"),
        pytest.param("abc", "qwe", "abcqwe", id="strings"),
    ])
    def test_add_multi(self, a, b, expected):
        s = Solver(a, b)
        assert s.add() == expected

    def test_add_invalid_params(self):
        s = Solver("a", 1)
        with pytest.raises(TypeError, match="can only concatenate str"):
            s.add()


def test_check_list():
    assert [] is not []
    assert [1, ] == [1, ]
