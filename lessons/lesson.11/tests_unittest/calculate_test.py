import unittest
from calculator import ExpressionCalculator

class TestExpressionCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = ExpressionCalculator()

    def test_addition(self):
        test_cases = [
            ("2 + 2", 4),
            ("5 + 3", 8),
            ("0 + 4", 4),
        ]
        for expression, expected in test_cases:
            with self.subTest(expression=expression, expected=expected):
                self.assertEqual(self.calculator.calculate(expression), expected)

    def test_subtraction(self):
        test_cases = [
            ("5 - 3", 2),
            ("10 - 7", 3),
            ("3 - 5", -2),
        ]
        for expression, expected in test_cases:
            with self.subTest(expression=expression, expected=expected):
                self.assertEqual(self.calculator.calculate(expression), expected)

    def test_multiplication(self):
        test_cases = [
            ("4 * 2", 8),
            ("3 * 3", 9),
            ("0 * 100", 0),
        ]
        for expression, expected in test_cases:
            with self.subTest(expression=expression, expected=expected):
                self.assertEqual(self.calculator.calculate(expression), expected)

    def test_division(self):
        test_cases = [
            ("9 / 3", 3),
            ("10 / 2", 5),
            ("100 / 4", 25),
        ]
        for expression, expected in test_cases:
            with self.subTest(expression=expression, expected=expected):
                self.assertEqual(self.calculator.calculate(expression), expected)

    def test_combined_operations(self):
        test_cases = [
            ("2 + 3 * 4 - 5 / 2", 11.5),
            ("10 / 2 + 3 * 3", 14.0),
            ("(2 + 3) * 4", 20),
            ("4 * (3 + 2)", 20),
            ("(2 + 3) * (4 - 2)", 10),
        ]
        for expression, expected in test_cases:
            with self.subTest(expression=expression, expected=expected):
                self.assertEqual(self.calculator.calculate(expression), expected)

    def test_invalid_expressions(self):
        test_cases = [
            "2 + + 3",
            "5 * - 2",
            "3 + * 4",
            "4 / / 2",
        ]
        for expression in test_cases:
            with self.subTest(expression=expression):
                with self.assertRaises(ValueError):
                    self.calculator.calculate(expression)

    def test_division_by_zero(self):
        test_cases = [
            "4 / 0",
            "10 / (5 - 5)",
        ]
        for expression in test_cases:
            with self.subTest(expression=expression):
                with self.assertRaises(ZeroDivisionError):
                    self.calculator.calculate(expression)

if __name__ == "__main__":
    unittest.main()
