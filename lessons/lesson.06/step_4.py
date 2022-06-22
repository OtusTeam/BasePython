class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, price={self.price})"

    def __repr__(self):
        return str(self)

    def make_discount(self, discount_percent):
        """
        Apply discount onto the product

        :param discount_percent: from 1 to 100
        :return: None
        """
        self.price *= (100 - discount_percent) / 100


def apply_discount(prdct, percent):
    prdct.price *= (100 - percent) / 100


# Product.make_discount = apply_discount


print(Product)
product = Product("Laptop", 1990)
print(product.__class__)
print(product.__class__.__name__)
print(str(product))
print(product)
print('abc')
print(str('abc'))
print(repr('abc'))
print(repr(product))

print(['abc', 123])
print([product])
p_smartphone = Product("Smartphone", 990)

print("before discount")
print(product)
print("apply discount 10")
product.make_discount(10)
print(product)
print("apply discount 20")
product.make_discount(20)
print(product)

print(p_smartphone)
print(id(p_smartphone))
p_smartphone.make_discount(5)
print(p_smartphone)
print(id(p_smartphone))

apply_discount(p_smartphone, 3)
print(p_smartphone)
