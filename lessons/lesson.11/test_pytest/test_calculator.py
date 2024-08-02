import pytest
from calculator import ExpressionCalculator

@pytest.fixture
def calculator():
    return ExpressionCalculator()


@pytest.mark.parametrize("expression, expected", [
    ("2 + 2", 4),
    ("5 + 3", 8),
    ("0 + 4", 4),
])
def test_addition(calculator, expression, expected):
    assert calculator.calculate(expression) == expected

@pytest.mark.parametrize("expression, expected", [
    ("5 - 3", 2),
    ("10 - 7", 3),
    ("3 - 5", -2),
])
def test_subtraction(calculator, expression, expected):
    assert calculator.calculate(expression) == expected

@pytest.mark.parametrize("expression, expected", [
    ("4 * 2", 8),
    ("3 * 3", 9),
    ("0 * 100", 0),
])
def test_multiplication(calculator, expression, expected):
    assert calculator.calculate(expression) == expected

@pytest.mark.parametrize("expression, expected", [
    ("9 / 3", 3),
    ("10 / 2", 5),
    ("100 / 4", 25),
])
def test_division(calculator, expression, expected):
    assert calculator.calculate(expression) == expected

@pytest.mark.parametrize("expression, expected", [
    ("2 + 3 * 4 - 5 / 2", 11.5),
    ("10 / 2 + 3 * 3", 14.0),
    ("(2 + 3) * 4", 20),
    ("4 * (3 + 2)", 20),
    ("(2 + 3) * (4 - 2)", 10),
])
def test_combined_operations(calculator, expression, expected):
    assert calculator.calculate(expression) == expected

@pytest.mark.parametrize("expression", [
    "2 + + 3",
    "5 * - 2",
    "3 + * 4",
    "4 / / 2",
])
def test_invalid_expressions(calculator, expression):
    with pytest.raises(ValueError):
        calculator.calculate(expression)

@pytest.mark.parametrize("expression", [
    "4 / 0",
    "10 / (5 - 5)",
])
def test_division_by_zero(calculator, expression):
    with pytest.raises(ZeroDivisionError):
        calculator.calculate(expression)

@pytest.mark.parametrize("expression, expected", [
    ("2 + 3 * 4 - 5 / 2", [2.0, '+', 3.0, '*', 4.0, '-', 5.0, '/', 2.0]),
    ("10 / 2 + 3 * 3", [10.0, '/', 2.0, '+', 3.0, '*', 3.0]),
    ("(2 + 3) * 4", ['(', 2.0, '+', 3.0, ')', '*', 4.0]),
    ("4 * (3 + 2)", [4.0, '*', '(', 3.0, '+', 2.0, ')']),
    ("(2 + 3) * (4 - 2)", ['(', 2.0, '+', 3.0, ')', '*', '(', 4.0, '-', 2.0, ')']),
])
def test_tokenize(calculator, expression, expected):
    assert calculator.tokenize(expression) == expected

if __name__ == '__main__':
    pytest.main()