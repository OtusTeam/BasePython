from src.model.expence import Expense


class Predictor:
    
    def __init__(self, expences: list[Expense]):
        self.expences = expences
        # to-do: валидация

# To-do: аналитические методы

    def total_expences(self):
        result = 0.0
        for expence in self.expences:
            result += expence.amount
        return result
        