class ProductMeta(type):
    def __new__(mcs, name, bases, attrs):
        new_class = super().__new__(mcs, name, bases, attrs)
        if 'screen_size' not in attrs:
            new_class.screen_size = None
        return new_class


class BaseProduct(metaclass=ProductMeta):
    type = None

    def __init__(self, name, price):
        self.name = name
        self.price = price


class Phone(BaseProduct):
    type = 'Phone'
    # screen_size = None


phone = Phone('Samsung Galaxy Note 10', 1000)
phone.screen_size = 5
print(phone.screen_size)

