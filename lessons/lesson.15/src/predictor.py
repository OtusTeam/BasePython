from src.model.expense import Expense


class Predictor:
    def __init__(self, expenses: list[Expense]):
        self.expenses = expenses

# TODO: валидация

    def total_expenses(self):
        result = 0
        for expense in self.expenses:
            result += expense.amount
        return result

