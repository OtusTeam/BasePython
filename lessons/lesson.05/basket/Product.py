class BaseProduct:
    type = None

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} ({self.type})"

    def __add__(self, other):
        return self.price + other.price

    def make_discount(self, discount):
        self.price *= (100 - discount)/100


class Laptop(BaseProduct):
    type = 'Laptop'


class MobilePhone(BaseProduct):
    type = 'Mobile Phone'


phone = MobilePhone('Samsung Galaxy Note 10', 1000)
laptop = Laptop('Macbook Pro 16"', 3500)

# Перегрузка оператора
# В Python нет перегрузки методов, есть overriding, но есть перегрузка операторов
basket = 0
basket = phone + laptop
print(basket)
