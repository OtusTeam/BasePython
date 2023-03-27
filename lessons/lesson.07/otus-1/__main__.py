# import utils
# from utils import get_currency_rate, BASE_CURRENCY, save_currency_rate
# import math, functools, itertools
import functools
import itertools
import math
import sys
# from math import *

# from numpy import *
from requests import get

# from utils import *
from helpers import get_currency_rate
from utils import (
    get_currency_rate, BASE_CURRENCY,
)


# print(dir(utils))
print(sys.path)


def main():
    print('started')
    # currency_rate = utils.get_currency_rate()
    currency_rate = get_currency_rate()
    print(currency_rate)
    # print(utils.BASE_CURRENCY)
    print(BASE_CURRENCY)
    print(min([1, 20]))
    print(math.sin(1.5), functools.partial, itertools.cycle)
    print(get)


if __name__ == '__main__':
    main()
