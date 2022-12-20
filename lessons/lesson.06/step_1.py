
class Product:

    TYPES = ['type1', 'type2']

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        # return f"{self.__class__.__name__}"
        return f"{type(self).__name__}(name={self.name!r}, price={self.price})"

    def __repr__(self):
        return str(self)

    def calc_discount_price(self, discount_percent: int) -> float:
        return self.price * (100 - discount_percent) / 100

    def make_discount(self, discount_percent: int) -> None:
        # self.price *= (100 - discount_percent) / 100
        self.price = self.calc_discount_price(discount_percent)


class Laptop(Product):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.touchscreen = False

    # def __init__(self, name, price):
    #     super().__init__(name, price)
    #     # Product.__init__(self, name, price)
    #     self.touchscreen = False


class Smartphone(Product):
    pass


print("Smartphone bases:", Smartphone.mro())
print("Laptop bases:", Laptop.mro())
print("Product bases:", Product.mro())


laptop = Laptop("Asus", 1999)
laptop_2 = Laptop("Acer", 2999)

smartphone = Smartphone("Samsung", 999)

print(laptop.__dict__)
print(laptop.TYPES)
laptop.touchscreen = True
print(laptop.__dict__)

# print(dir(laptop))


# smartphone.cellular_5g = True

# print(laptop, laptop.name, repr(laptop.name), f'{laptop.name!r}', f'{laptop.name}')
print(laptop, laptop.touchscreen)
print(laptop_2, laptop_2.touchscreen)
# print(smartphone, smartphone.cellular_5g)
print(smartphone)
smartphone.make_discount(10)
print(smartphone)
smartphone.make_discount(20)
print(smartphone)

print([laptop, smartphone])
