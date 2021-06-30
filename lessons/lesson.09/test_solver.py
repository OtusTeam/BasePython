from unittest import TestCase

import pytest

from solver import Solver2D, from_dict2


class TestSolver2DTestCase(TestCase):

    def setUp(self) -> None:
        self.solver = Solver2D(4, 5)

    def test_add(self):
        res = self.solver.add()
        self.assertEqual(res, 9)

    def test_add_after_mutation(self):
        self.solver.a = 10
        self.assertEqual(self.solver.add(), 15)

    def test_mul(self):
        res = self.solver.mul()
        self.assertEqual(res, 20)

    def test_add_raises_type_error(self):
        s = Solver2D(1, "2")

        with self.assertRaises(TypeError) as exc_info:
            s.add()

        self.assertEqual(
            str(exc_info.exception),
            Solver2D.EXC_VALUES_HAVE_TO_BE_NUMS,
        )


class TestSolver2D:

    @classmethod
    def gen_solver(cls):
        return Solver2D(2, 3)

    def test_mul(self):
        s = self.gen_solver()
        res = s.mul()
        assert res == 6

    def test_add(self):
        s = self.gen_solver()
        res = s.add()
        assert res == 5

    def test_add_raises_type_error(self):
        s = self.gen_solver()
        s.b = "2"

        with pytest.raises(TypeError) as exc_info:
            s.add()

        assert str(exc_info.value) == Solver2D.EXC_VALUES_HAVE_TO_BE_NUMS


def test_from_dict2():
    a = 1
    b = 2
    s = from_dict2({"a": a, "b": b})
    assert s.a == a
    assert s.b == b
