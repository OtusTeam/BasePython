from src.predictor import Predictor
from src.model import Expense
from src.storage import open_file
from pathlib import Path

CURR_DIR = Path.cwd()

def main():
    # expense = Expense("1990-10-10", "food", 21.1)
    # print(expense)
    print(CURR_DIR / "src" / "data" / "sample.csv")
    expences = open_file(CURR_DIR / "src" / "data" / "sample.csv")
    print(expences)

    predictor = Predictor(expences)
    print(predictor.total_expences())

if __name__ == "__main__":
    main()
    