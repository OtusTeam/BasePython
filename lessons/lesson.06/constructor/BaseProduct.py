class BaseProduct:

    def __new__(cls, *args, **kwargs):
        print("__new__ is called")
        print(cls)
        print(args)
        print(kwargs)
        return super().__new__(cls)

    def __init__(self, price):
        print("__init__ is called")
        self._price = price


class Phone(BaseProduct):
    pass


phone = Phone(1000)


