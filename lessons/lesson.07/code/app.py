"""
Main app module
"""
# import math, random, functools
import functools
import math
import random

import numpy as np

import orders
# from orders import *
# from orders.create_it import create_special


def setup_db():
    print('db init')


def main():
    setup_db()
    print('server started')
    orders.create()
    orders.create_special()
    orders.update()
    orders.delete()


# print(__name__)
# print(globals())
if __name__ == '__main__':
    main()
