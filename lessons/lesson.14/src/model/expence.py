"""
В этом файле сущность траты
"""

from datetime import datetime


class Expense:

    def __init__(self, date: str, category: str, amount: float):
        self.validate(date, category, amount)
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.category = category.strip().lower()
        self.amount = float(amount)

    def validate(self, date, category, amount):
        if not isinstance(date, str):
            raise TypeError("Неправильный тип data")
        if not isinstance(category, str):
            raise TypeError("Неправильный тип category")
        if not isinstance(amount, float):
            raise TypeError(f"Неправильный тип amount {amount = }")

    def __repr__(self):
        return f"{self.date = } {self.category = } {self.amount = }"

    def __str__(self):
        return f"{self.date = } {self.category = } {self.amount = }"
