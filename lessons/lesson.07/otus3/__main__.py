import sys
# import os
import pathlib

ROOT = pathlib.Path(__file__).parent.parent
sys.path.append(str(ROOT))
# import django

from currency import currency_rate
from db import save_rate
from helpers import say_hello
from utils import write_log


def main():
    print('started')
    write_log('started')
    say_hello()
    currency = 'USD'
    today_rate = currency_rate(currency)
    print(f'rate is {today_rate}')
    save_rate(currency, today_rate)
    print('finished')


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
        exit(2)
