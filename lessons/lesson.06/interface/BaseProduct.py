class BaseProduct:

    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._calc_price()

    @price.setter
    def price(self, price):
        self._price = price

    # надо реализовать в наследниках
    def _calc_price(self):
        print('calc price is called')
        # return self._price


class Phone(BaseProduct):
    def _calc_price(self):
        return self._price


class Notebook(BaseProduct):
    pass


phone = Phone(100)
print(phone.price)
notebook = Notebook(1000)
print(notebook.price)
