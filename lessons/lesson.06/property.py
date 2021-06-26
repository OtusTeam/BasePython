class BaseProduct:
    type = None

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name} (type = {self.type}, price = {self.price})'

    def __repr__(self):
        return f"{self.__class__.__name__} ('{self.name}', {self.price})"


class Laptop(BaseProduct):
    pass


class MobilePhone(BaseProduct):
    pass


class Basket:

    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items

    def __iadd__(self, product):
        self._items.append(product)
        return self

    def add(self, product):
        self._items.append(product)


basket = Basket()
print(basket.items)
