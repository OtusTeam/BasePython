class Product:
    product_kind = None

    def __init__(self, name, price):
        self._name = name
        self._price = float(price)

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
    product_kind = 'notebook'

    def __init__(self, name, price, a_capacity=0):
        super().__init__(name, price)

        self.a_capacity = a_capacity


class Phone(Product):
    product_kind = 'phone'

    def to_html(self):
        return f'<h2>"{self.product_kind}": {self._name} <b>{self._price}</b></h2>'


prod_1 = Phone('iPhone', 1988.64)
prod_2 = Notebook('MacBook', 2789.64, 5300)
prod_2.make_discount(5)
print(prod_2.a_capacity)
print(prod_1.to_html())
print(prod_2.to_html())
