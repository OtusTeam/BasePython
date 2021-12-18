class BaseProduct:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.__class__.__name__}: (name = {self.name}, price = {self.price})"

    def __repr__(self):
        return f"{self.__class__.__name__} ('{self.name}', {self.price})"


class Laptop(BaseProduct):
    pass


class MobilePhone(BaseProduct):
    pass


product = BaseProduct('Calculator', 10)
laptop = Laptop('Macbook Pro 16', 2500)
nokia = MobilePhone('Nokia 3310', 20)
print(type(nokia))
nokia_repr = repr(nokia)
print(type(nokia_repr))
print(nokia_repr)
nokia_obj = eval(nokia_repr)
print(type(nokia_obj))
print(nokia_obj)
