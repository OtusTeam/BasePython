class Product:
    def __init__(self, price):
        print('Product Initializer is called')

    def test(self):
        print('Product')


class Drink:

    def test(self):
        print('Drink')


class Milk(Drink, Product):
    def __init__(self, price, calories):
        super().__init__(price)
        self.calories = calories

    def super_test(self):
        super().test()


milk = Milk(1, 10)
print(Milk.mro())
