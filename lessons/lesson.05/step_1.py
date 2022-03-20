# class Product(object):
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


prod_1 = Product('iPhone', 1988.64)  # instance, object
print(prod_1)
print(prod_1.name)
print(prod_1.price)
