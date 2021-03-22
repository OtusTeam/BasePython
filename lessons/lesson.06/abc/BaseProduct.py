from abc import ABC, abstractmethod

# abc - Abstract Base Classes
class BaseProduct(ABC):

    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._calc_price()

    @price.setter
    def price(self, price):
        self._price = price

    @abstractmethod     # дубинка
    def _calc_price(self):
        pass


class Notebook(BaseProduct):
    pass


notebook = Notebook(15)
print(notebook.price)
