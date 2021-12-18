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
        self._discount = 0

    @property
    def items(self):
        return self._items

    @property
    def discount(self):
        print('discount getter is called')
        return self._discount

    @discount.setter
    def discount(self, val):
        if val < 0 or val > 100:
            raise BaseException('Discount is not valid')
        print('discount setter is called')
        self._discount = val

    def get_items(self):
        return self._items

    def __iadd__(self, product):
        self._items.append(product)
        return self

    def add(self, product):
        self._items.append(product)


laptop = Laptop("Hp", 700)

basket = Basket()
print(basket.items)
# items = basket.get_items()
# basket.items = ['Apple']
basket.add(laptop)
# basket += laptop
# print(basket.items)
# basket.discount = -19
basket._discount = -19
print(basket.discount)
