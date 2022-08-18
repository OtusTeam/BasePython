class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product(name={self.name!r}, price={self.price})"

    def __repr__(self):
        return str(self)
        # return "Product"

    def make_discount(self, discount_percent):
        """
        Applies discount in %
        :param discount_percent:
        :return:
        """
        self.price *= (100 - discount_percent) / 100


# def init_product(product, name, price):
#     product.name = name
#     product.price = price
#
#
# Product.__init__ = init_product

product_laptop = Product("Laptop 1", 2000)
# init_product(product_laptop, "Laptop 2", 2999)

print(product_laptop.name)
print(repr(product_laptop.name))
print(product_laptop.price)
print(product_laptop.__dict__)

print(type(product_laptop))
print(product_laptop)
print(repr(product_laptop))


product_smartphone = Product("Smartphone 1", 1000)

print(product_smartphone)
print(product_laptop)

product_smartphone.make_discount(10)
product_laptop.make_discount(20)

print(product_smartphone)
print(product_laptop)
