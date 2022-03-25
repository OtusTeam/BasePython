class RateError(Exception):
    pass


class PriceError(Exception):
    pass


class Product:
    product_kind = None

    def __init__(self, name, price):
        self.name = name
        try:
            self.__price = float(price)  # private
        except ValueError:
            raise PriceError(price)

    def __str__(self):
        return f'{self.name} ({self.__price})'

    @staticmethod
    def convert_price(price, rate):
        if rate <= 0:
            raise RateError(rate)
            # raise ValueError(rate)
        return price * rate

    @classmethod
    def create_converted(cls, name, price, rate):
        return cls(name, cls.convert_price(price, rate))


class Notebook(Product):
    product_kind = 'notebook'

    def __init__(self, name, price, a_capacity=0):
        super().__init__(name, price)

        self.a_capacity = a_capacity


class Phone(Product):
    product_kind = 'phone'

    def __str__(self):
        # parent_str = super().__str__()
        # return f'{self.name} [{self.__price}]'
        return f'{self.name} [{self._Product__price}]'  # NEVER


prod_1 = Phone('iPhone', '1988.64')
prod_1.__price = 157
print(vars(prod_1))
print(prod_1)
