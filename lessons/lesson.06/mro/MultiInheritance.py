class Product:
    def __init__(self, price):
        self.price = price
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

    def test(self):
        print('Milk')


milk = Milk(1, 10)
milk.test()
# MRO - Method Resolution Order
print(Milk.mro())
