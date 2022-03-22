class Product:
    product_kind = None

    def __init__(self, name, price):
        self.name = name
        self.price = float(price)

    def __add__(self, other):
        # if not isinstance(other, self.__class__):
        #     raise TypeError
        # return self.price + other.price
        return Product('sum', self.price + other.price)

    def __str__(self):
        return f'{self.name} ({self.price})'

    def __len__(self):
        return len(self.name)

    # def add(self, other):
    #     pass
    #
    # def add_it(self, other):
    #     pass
    # def to_str(self):
    #     pass


class Notebook(Product):
    product_kind = 'notebook'

    def __init__(self, name, price, a_capacity=0):
        super().__init__(name, price)

        self.a_capacity = a_capacity


class Phone(Product):
    product_kind = 'phone'


prod_1 = Phone('iPhone', 1988.64)
prod_2 = Notebook('MacBook', 2789.64, 5300)
prod_3 = Phone('Galaxy S22', 2478.4)
# basket_price = prod_1 + prod_2
# basket_price = prod_2 + prod_1
# + - * / += -= *= /= - or and
basket_price = prod_1 + prod_2 + prod_3
# basket_price = prod_1.__add__(prod_2).__add__(prod_3)
# print(str(basket_price))
print(basket_price)
# prod_1()
print(len(prod_1))
