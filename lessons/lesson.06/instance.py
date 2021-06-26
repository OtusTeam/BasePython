class BaseProduct:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __add__(self, other):
        return BaseProduct("BaseProduct", self.price + other.price)


class Laptop(BaseProduct):
    pass


class MobilePhone(BaseProduct):
    pass


samsung_note_10 = MobilePhone('Samsung Galaxy Note 10', 1000)
mac_pro = Laptop('Macbook Pro 16"', 3500)
nokia = MobilePhone("Nokia 3310", 50)

basket = samsung_note_10 + nokia + mac_pro
print(basket.price)

