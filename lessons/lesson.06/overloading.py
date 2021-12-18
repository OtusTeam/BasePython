class BaseProduct:

    def __init__(self, name, price):
        print("__init__ started")
        self.name = name
        self.price = price

    def __add__(self, other):
        return self.price + other.price

    def __str__(self):
        print('__str__ started')
        return f"{self.__class__.__name__}: (name = {self.name}, price = {self.price})"


class Laptop(BaseProduct):
    pass


class MobilePhone(BaseProduct):
    pass


# product = BaseProduct.__init__('Calculator', 10)
product = BaseProduct('Calculator', 10)
laptop = Laptop('Macbook Pro 16', 2500)
phone = MobilePhone('Nokia 3310', 20)
# print(BaseProduct.__str__(product))
print(product)

basket = product + phone
print(basket)
