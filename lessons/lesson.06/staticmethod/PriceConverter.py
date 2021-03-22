class BaseProduct:

    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    @staticmethod
    def convert_price(price, ratio):
        return price * ratio



class Phone(BaseProduct):
    pass


phone = Phone(BaseProduct.convert_price(1, 44))
print(phone.price)



