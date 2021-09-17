
class BaseProduct:
    type = None

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} (type = {self.type}, price = {self.price})"


class Laptop(BaseProduct):
    type = 'Laptop'


class MobilePhone(BaseProduct):
    type = 'Mobile Phone'


samsung_note_10 = MobilePhone('Samsung Galaxy Note 10', 1000)
mac_pro = Laptop('Macbook Pro 16"', 3500)
nokia = MobilePhone("Nokia 3310", 50)

basket = []
basket = [samsung_note_10, mac_pro, nokia]
# for item in basket:
#     print(basket)
print(samsung_note_10)
print(mac_pro)
print(basket)
