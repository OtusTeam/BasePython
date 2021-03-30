class BaseProduct:
    type = None

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name} (type = {self.type}, price = {self.price})'

    def __repr__(self):
        return f"{self.__class__.__name__} ('{self.name}', {self.price})\n"

    def __add__(self, other):
        # return self.__class__(self.price + other.price)
        return BaseProduct('BaseProduct', self.price + other.price)

    def make_discount(self, discount):
        self.price *= (100 - discount) / 100


class Laptop(BaseProduct):
    type = 'Laptop'


class MobilePhone(BaseProduct):
    type = 'Mobile Phone'


class Basket:

    def __init__(self):
        self.items = []

    def __iadd__(self, product):
        self.items.append(product)
        return self

    def add(self, product):
        self.items.append(product)


samsung_note_10 = MobilePhone('Samsung Galaxy Note 10', 1000)
mac_pro = Laptop('Macbook Pro 16"', 3500)
nokia = MobilePhone("Nokia 3310", 50)

basket = Basket()
basket += samsung_note_10
basket += mac_pro
basket += nokia

basket.add(samsung_note_10)
basket.add(mac_pro)
basket.add(nokia)

print(basket.items)
print(len(basket.items))
