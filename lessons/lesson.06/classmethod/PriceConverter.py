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

    # @staticmethod
    # def create_converted(price, ratio):
    #     return BaseProduct(BaseProduct.convert_price(price, ratio))

    @classmethod  # - особый статический метод
    def create_converted(cls, price, ratio):
        return cls(cls.convert_price(price, ratio))


class Phone(BaseProduct):
    pass


class Notebook(BaseProduct):
    pass


product = BaseProduct.create_converted(1, 44)
print(type(product))
phone = Phone.create_converted(1, 44)
print(type(phone))
notebook = Notebook.create_converted(1000, 44000)
print(type(notebook))
