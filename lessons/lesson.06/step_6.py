class Product:
    product_kind = None

    def __init__(self, name, price):
        self.name = name
        self.price = float(price)

    def __str__(self):
        return f'{self.name} ({self.price})'


class Notebook(Product):
    product_kind = 'notebook'

    def __init__(self, name, price, a_capacity=0):
        super().__init__(name, price)

        self.a_capacity = a_capacity


class Phone(Product):
    product_kind = 'phone'


def convert_price(price, rate):
    return price * rate


prod_1 = Phone('iPhone', 1988.64)
prod_2 = Notebook('MacBook', convert_price(2789.64, 2.7), 5300)
prod_3 = Phone('Galaxy S22', convert_price(2478.4, 2.7))

print(prod_1.price)
print(prod_2.price)
print(prod_3.price)

