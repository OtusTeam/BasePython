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


class Basket:

    # protected - защищенное
    # private - приватное
    def __init__(self):
        self.items = []
        self._discount = 0

    def add(self, new_item):
        self.items.append(new_item)


product = BaseProduct('Calculator', 10)
laptop = Laptop('Macbook Pro 16', 2500)
nokia = MobilePhone('Nokia 3310', 20)

basket = Basket()
print(basket.items)
basket.items.append(product)
basket.items.append(laptop)
basket.items.append(7)
basket.add(nokia)
basket.discount = 200
# discount, _discount
print(basket._discount)
print(basket.items)

