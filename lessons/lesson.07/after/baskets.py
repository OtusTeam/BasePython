class Basket:

    def __init__(self):
        self._discount = 0

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, percentage):

        try:
            self._discount = float(percentage)
        except Exception as ex:
            print(ex)
            raise PriceValueError(percentage)


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
