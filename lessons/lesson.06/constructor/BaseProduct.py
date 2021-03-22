class BaseProduct:

    def __new__(cls, *args, **kwargs):
        print(cls)
        print(args)
        print(kwargs)
        return super().__new__(cls)

    def __init__(self, price):
        self._price = price



class Phone(BaseProduct):
    pass


phone = Phone(BaseProduct.convert_price(1, 44))



