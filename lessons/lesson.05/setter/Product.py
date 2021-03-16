
class BaseProduct:
    type = None

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name} (type = {self.type}, price = {self.price})'

    def __repr__(self):
        return f"{self.__class__.__name__} ('{self.name}', {self.price})"

    def __add__(self, other):
        # return self.__class__(self.price + other.price)
        return BaseProduct('BaseProduct', self.price + other.price)

    def make_discount(self, discount):
        self.price *= (100 - discount)/100


class Laptop(BaseProduct):
    type = 'Laptop'


class MobilePhone(BaseProduct):
    type = 'Mobile Phone'

class Basket:

    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, val):
        self.__iadd__(val)

    def __iadd__(self, product):
        self._items.append(product)
        return self

    def add(self, product):
        self._items.append(product)

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return (el for el in self._items)


samsung_note_10 = MobilePhone('Samsung Galaxy Note 10', 1000)
mac_pro = Laptop('Macbook Pro 16"', 3500)
nokia = MobilePhone("Nokia 3310", 50)

basket = Basket()
print(basket.items)
basket.items = nokia
print(basket)
print(nokia in basket.items)





