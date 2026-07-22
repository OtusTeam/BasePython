"""Модели расходов и рассчет прогнозов."""


from datetime import datetime


class Expense:
    """Трата - одна строка из csv."""
    def __init__(self, date: str, category: str, amount: str):
        self.validate(date, category, amount)
        self.date = datetime.strptime(date, '%Y-%m-%d')
        self.category = category.strip().lower()
        self.amount = float(amount)

    def validate(self, date: str, category: str, amount: str):
        if not isinstance(date, str):
            raise TypeError("Неправильный тип date")
        if not isinstance(category, str):
            raise TypeError("Неправильный тип category")
        if not isinstance(amount, str):
            raise TypeError("Неправильный тип amount")

    # def validate_item(self, item, obj):
    #     if not isinstance(item, obj):
    #         raise TypeError(f"Неправильный тип {item}")

    def __repr__(self):
        """..."""
        return f"Expense(date='{self.date}', category='{self.category}', amount='{self.amount}')"

    def __str__(self):
        """..."""
        return f"{self.date=} {self.category=}, {self.amount=}"


if __name__ == '__main__':
    e = Expense("2024-04-01", "food ", "100")
    print(e)