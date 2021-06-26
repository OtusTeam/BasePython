class BaseProduct:

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
        # -> _attr - protected - снаружи трогать нельзя

    def __iadd__(self, product):
        self._items.append(product)
        return self

    def add(self, product):
        self._items.append(product)


samsung_note_10 = MobilePhone('Samsung Galaxy Note 10', 1000)
mac_pro = Laptop('Macbook Pro 16"', 3500)
nokia = MobilePhone("Nokia 3310", 50)

basket = Basket()
basket._items.append(nokia)
print(basket._items)
