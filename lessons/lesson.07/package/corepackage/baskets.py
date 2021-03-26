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

