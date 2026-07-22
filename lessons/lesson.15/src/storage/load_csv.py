"""Чтение расходов из csv."""


import csv
from pathlib import Path
from src.model.expense import Expense


def open_file(file_path: Path) -> list[Expense]:
    result = []
    # print(f'{file_path=}')
    with open(file_path, 'r', encoding="UTF-8", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        headers = reader.fieldnames
        validate_header(headers)

        for row in reader:
            date = row.get("date")
            category = row.get("category")
            amount = row.get("amount")
            expense = Expense(date, category, amount)
            result.append(expense)

    return result


def validate_header(headers):
    if headers is None:
        raise ValueError('CSV не содержит заголовков')
    if not ("date" in headers and "category" in headers and "amount" in headers):
        raise ValueError('CSV не содержит нужного заголовка')


if __name__ == '__main__':
    # open_file("data\sample.csv")
    pass