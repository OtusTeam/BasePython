class Product:
    def __init__(self, name, price):
        self._name = name  # public -> immutable
        # self.price = price
        # self._price = price  # protected
        self._price = float(price)

    @property
    def name(self):
        return self._name

    @property
    def price(self):  # getter
        # heavy calcs
        return self._price

    @price.setter
    def price(self, value):  # setter
        # if not isinstance(value, (int, float)):
        #     raise ValueError(f'wrong type for {value}: {type(value)}')
        self._price = float(value)

    def make_discount(self, discount):
        """discount: in percents"""
        self._price *= (100 - discount) / 100

    def to_html(self):
        return f'<h1>{self._name} <b>{self._price}</b></h1>'

    # name = property(...)


# prod_1 = Product('iPhone', 1988.64)
prod_1 = Product('iPhone', '1988.64')
print(prod_1.price)

# prod_1.price = '1578.21 rub'
# prod_1.price = '1578.21'
# prod_1.price = 1578.21
prod_1.make_discount(5)

print(prod_1.price)
print(prod_1.name)

prod_1._name = 'Galazy S22'
print(prod_1.name)
