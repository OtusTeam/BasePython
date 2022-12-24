# from math import (
#     pi, sin, cos, tan, tanh,
#     log2, log10, floor,
# )
# import math, random
import math
import random

import numpy as np

# import settings
# import currency
from currency import currency_rate
from db import save_rate
from helpers import say_hello


def main():
    print('started')
    say_hello()
    currency = 'USD'
    today_rate = currency_rate(currency)
    print(f'rate is {today_rate}')
    save_rate(currency, today_rate)
    print(max([100, 200, 1000]))
    # print(pi, floor(pi))
    print(math.pi, np.pi, math.floor(math.pi))
    print('finished')


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
        exit(2)
