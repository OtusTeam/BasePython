from main import Solver, dev
import unittest


# Unittest
class SolverTestCase(unittest.TestCase):

    def setUp(self) -> None:
        print('Я выполняюсь перед каждым тестом')
        self.solver = Solver(3, 4)

    def test_add(self):
        solver = Solver(1, 2)
        self.assertEqual(solver.add(), 3)

        self.assertEqual(self.solver.add(), 7)

    def test_mul(self):
        self.assertEqual(self.solver.mul(), 12)


class DevTestCase(unittest.TestCase):

    def test_dev(self):
        self.assertEqual(dev(4, 2), 2)

    def test_dev_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            dev(10,0)


