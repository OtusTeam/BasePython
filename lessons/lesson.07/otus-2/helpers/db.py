import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
print(ROOT)
sys.path.append(str(ROOT))

from utils import save_currency_rate
# from ..utils import save_currency_rate


def update_db():
    return save_currency_rate('USD', 15)


if __name__ == '__main__':
    print(update_db())
