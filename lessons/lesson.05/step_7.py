class Product:
    product_kind = None

    def __init__(self, name, price, product_kind=None):
        self._name = name
        self._price = float(price)
        self.product_kind = product_kind

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):  # setter
        self._price = float(value)

    def make_discount(self, discount):
        """discount: in percents"""
        self._price *= (100 - discount) / 100

    def to_html(self):
        return f'<h1>"{self.product_kind}": {self._name} <b>{self._price}</b></h1>'


class Notebook(Product):
    pass


class Phone(Product):
    pass


class PhonoBook(Notebook, Phone):
    pass


prod_1 = Phone('iPhone', 1988.64, 'phone')
prod_2 = Notebook('MacBook', 2789.64)
print(vars(prod_1))
print(prod_1.to_html())
print(vars(prod_2))
print(prod_2.to_html())

