class BaseProduct:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name} (price = {self.price})'

    def __repr__(self):
        return f"{self.__class__.__name__} ('{self.name}', {self.price})"


class Laptop(BaseProduct):
    pass


class MobilePhone(BaseProduct):
    pass


samsung_note_10 = MobilePhone('Samsung Galaxy Note 10', 1000)
mac_pro = Laptop('Macbook Pro 16"', 3500)
nokia = MobilePhone("Nokia 3310", 50)

basket = 0
print(samsung_note_10)
basket = [samsung_note_10, mac_pro, nokia]
print(basket)
nokia_clone = eval(repr(nokia))
print(nokia_clone.price)
