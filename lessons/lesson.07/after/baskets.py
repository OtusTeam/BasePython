class Basket:
    pass


class PriceValueError(Exception):
    pass

# Если делать import baskets, будет ли выполняться этот код ?
# А если делать from baskets import *
# from baskets import Basket, PriceValueError
# print("testing imports")

# print(__name__)

# Если запускать из app.py - не выполнится код в конструкции main
# if __name__ == '__main__':
#     print('testing imports')
