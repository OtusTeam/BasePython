import functools
import itertools
import math

from requests import get

# from helpers import get_currency_rate
# from helpers.new.
from helpers.currency import get_currency_rate
from helpers.db import update_db
from utils import (
    get_currency_rate, BASE_CURRENCY,
)


def main():
    print('started')
    currency_rate = get_currency_rate()
    print(currency_rate)
    print(BASE_CURRENCY)
    print(min([1, 20]))
    print(math.sin(1.5), functools.partial, itertools.cycle)
    print(get)
    print(update_db)


if __name__ == '__main__':
    main()
