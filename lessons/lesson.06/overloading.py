class BaseProduct:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} ({self.type})"

    def __add__(self, other):
        return self.price + other.price

    # def test(self, first):
    #     pass
    #
    # def test(self, first, second):
    #     pass
    #
    # def test(self, first, second, third):
    #     pass


class Laptop(BaseProduct):
    pass


class MobilePhone(BaseProduct):
    pass


phone = MobilePhone('Samsung Galaxy Note 10', 1000)
laptop = Laptop('Macbook Pro 16"', 3500)

# Перегрузка оператора
# В Python нет перегрузки методов, есть overriding, но есть перегрузка операторов
basket = phone + laptop
print(basket)
