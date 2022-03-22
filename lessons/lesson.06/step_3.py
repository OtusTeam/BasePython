class Product:
    product_kind = None

    def __init__(self, name, price):
        self.name = name
        self.price = float(price)

    def __str__(self):
        return f'{self.name} ({self.price})'


class Notebook(Product):
    product_kind = 'notebook'

    def __init__(self, name, price, a_capacity=0):
        super().__init__(name, price)

        self.a_capacity = a_capacity


class Phone(Product):
    product_kind = 'phone'


class Basket:
    def __init__(self):
        self._items = {}

    def __setitem__(self, key, value):
        self._items[key.name] = value
        # self._items[key.name] = (key, value)

    def __getitem__(self, item):
        return self._items[item.name]

    def __len__(self):
        # return len(self._items)
        return sum(self._items.values())


class SmallBasket(Basket):
    pass


prod_1 = Phone('iPhone', 1988.64)
prod_2 = Notebook('MacBook', 2789.64, 5300)
prod_3 = Phone('Galaxy S22', 2478.4)

# basket_1 = Basket()
basket_1 = SmallBasket()
basket_1[prod_1] = 3
basket_1[prod_2] = 2
basket_1[prod_3] = 1

print(basket_1[prod_2])
print(len(basket_1))
