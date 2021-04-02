class ProductMeta(type):
    def __new__(mcs, name, bases, attrs):
        print('Before:', attrs)
        # print(type(attrs))
        # attrs['name'] = 'Test'
        new_class = super().__new__(mcs, name, bases, attrs)
        if 'screen_size' not in attrs:
            new_class.screen_size = 5
        new_class.NAME = 'DEFAULT NAME'

        return new_class


# metaclass - type -> class -> instance
class BaseProduct(metaclass=ProductMeta):
    type = None

    def __init__(self, name, price):
        self.name = name
        self.price = price


    def __str__(self):
        return f'{self.name}'



class Phone(BaseProduct):
    type = 'Phone'
    # screen_size = None

    def __str__(self):
        return f'{self.name}'


phone = Phone('Samsung Galaxy Note 10', 1000)
base = BaseProduct('Base Product', 1000)
base.screen_size = 10
phone.screen_size = 5
print(phone)
print(base)



