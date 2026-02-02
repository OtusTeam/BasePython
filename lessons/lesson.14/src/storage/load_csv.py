import csv
from pathlib import Path
from src.model import Expense


def open_file(filepath: Path) -> list[Expense]:
    result = []
    print(f"{filepath = }")
    with open(filepath, "r", encoding="UTF-8", newline="") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames
        validate_header(headers)
        for row in reader:
            date = row.get("date")
            category = row.get("category")
            amount = float(row.get("amount"))
            expense = Expense(date, category, amount)
            result.append(expense)

    return result

def validate_header(headers):
    if headers is None:
        raise ValueError("CSV файл не содержит заголовка!")
    if not ("date" in headers and "category" in headers and "amount" in headers):
        raise ValueError(f"CSV не содержит нужного заголовка! {headers = }")
