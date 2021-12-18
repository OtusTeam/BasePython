class BaseProduct:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __add__(self, other):
        return self.price + other.price

    def __str__(self):
        return f"{self.__class__.__name__}: (name = {self.name}, price = {self.price})"


class Laptop(BaseProduct):
    pass


class MobilePhone(BaseProduct):
    pass


product = BaseProduct('Calculator', 10)
laptop = Laptop('Macbook Pro 16', 2500)
phone = MobilePhone('Nokia 3310', 20)
print(product)

basket = product + phone + laptop
print(basket)
