"""Точка входа."""


from pathlib import Path
from pprint import pprint
from src.model.expense import Expense
from src.storage.load_csv import open_file
from src.predictor import Predictor


def main():
    # e = Expense("2024-04-01", "food ", "101")
    # print(e)

    CURR_DIR = Path.cwd()
    path_file = CURR_DIR / "data" / "sample.csv"
    print(path_file)
    expenses = open_file(path_file)
    # pprint(expenses)

    predictor = Predictor(expenses)
    print(predictor.total_expenses())



if __name__ == '__main__':
    main()
