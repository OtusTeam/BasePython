class BaseProduct:
    type = None

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} (type = {self.type}, price = {self.price})"

    def __add__(self, other):
        # return self.__class__(self.price + other.price)
        # BaseProduct('BaseProduct', self.price + other.price)
        # product = BaseProduct('BaseProduct', self.price + other.price)
        return BaseProduct('BaseProduct', self.price + other.price)

    def make_discount(self, discount):
        self.price *= (100 - discount) / 100


class Laptop(BaseProduct):
    type = 'Laptop'


class MobilePhone(BaseProduct):
    type = 'Mobile Phone'


samsung_note_10 = MobilePhone('Samsung Galaxy Note 10', 1000)
mac_pro = Laptop('Macbook Pro 16"', 3500)
nokia = MobilePhone("Nokia 3310", 50)

basket = 0
basket = [samsung_note_10, mac_pro, nokia]
for product in basket:
    print(product)
print(basket)
