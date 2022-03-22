class Product:
    product_kind = None

    def __init__(self, name, price):
        self.name = name
        self.price = float(price)

    def __str__(self):
        return f'{self.name} ({self.price})'

    @staticmethod
    def convert_price(price, rate):
        return price * rate

    @staticmethod
    def create_converted(name, price, rate):
        return Product(name, Product.convert_price(price, rate))


class Notebook(Product):
    product_kind = 'notebook'

    def __init__(self, name, price, a_capacity=0):
        super().__init__(name, price)

        self.a_capacity = a_capacity


class Phone(Product):
    product_kind = 'phone'


prod_1 = Phone('iPhone', 1988.64)
# prod_2 = Notebook('MacBook', Notebook.convert_price(2789.64, 2.7), 5300)
prod_2 = Notebook.create_converted('MacBook', 2789.64, 2.7)
prod_3 = Phone.create_converted('Galaxy S22', 2478.4, 2.7)

# prod_2.price = prod_2.convert_price(prod_2.price, 27)

print(prod_1.price)
print(prod_2.price)
print(prod_3.price)

print(type(prod_2))
print(type(prod_3))
