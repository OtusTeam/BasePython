class RateError(Exception):
    pass


class PriceError(Exception):
    pass


class Product:
    product_kind = None

    def __init__(self, name, price):
        self.name = name
        # if not isinstance(price, (float, int)):
        #     raise PriceError(price)
        try:
            self.price = float(price)
        except ValueError:
            raise PriceError(price)

    def __str__(self):
        return f'{self.name} ({self.price})'

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


def main():
    prod_1 = Phone('iPhone', '1988.64 rub')
    # prod_2 = Notebook('MacBook', Notebook.convert_price(2789.64, 2.7), 5300)
    prod_2 = Notebook.create_converted('MacBook', 2789.64, 2.7)
    # try:
    prod_3 = Phone.create_converted('Galaxy S22', 2478.4, -2.7)

    # prod_2.price = prod_2.convert_price(prod_2.price, 27)

    print(prod_1.price)
    print(prod_2.price)
    print(prod_3.price)

    print(type(prod_2))
    print(type(prod_3))


if __name__ == '__main__':
    try:
        main()
    except RateError as e:
        print(e)
        exit(3)
    except PriceError as e:
        print(e)
        exit(4)
    except (ValueError, TypeError) as e:
        print(e)
        exit(2)
    except Exception as e:
        print(e)
        exit(1)
    else:
        print('ok')
    finally:
        print('bye')
