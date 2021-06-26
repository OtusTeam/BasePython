class BaseProduct:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Laptop(BaseProduct):
    pass


class MobilePhone(BaseProduct):
    pass


class Basket:

    def __init__(self):
        self.items = []

    def __iadd__(self, product):
        self.items.append(product)
        return self

    def __len__(self):
        return len(self.items)

    def add(self, product):
        self.items.append(product)


samsung_note_10 = MobilePhone('Samsung Galaxy Note 10', 1000)
mac_pro = Laptop('Macbook Pro 16"', 3500)
nokia = MobilePhone("Nokia 3310", 50)

basket = Basket()
basket += samsung_note_10
basket += mac_pro
basket += nokia

print(len(basket.items))
print(len(basket))
