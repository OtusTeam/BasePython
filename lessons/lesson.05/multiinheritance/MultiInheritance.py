class Product:

    def __init__(self, price):
        print("Product Initializer is called")
        self.price = price

    def test(self):
        print('Product')


    def product_test(self):
        print('Product Test')


class Drink:

    # def __init__(self, price, calories):
    #     print("Drink Initializer is called")
    #     self.price = price
    #     self.calories = calories


    def test(self):
        print('Drink')


class Milk(Drink, Product):

    def __init__(self, price, calories):
        # super().__init__(price, calories)
        # super().__init__(price, discount)
        super().__init__(price)

    def super_test(self):
        super().test()
        super().product_test()



milk = Milk(1, 10)

# milk.test()
# milk.super_test()

print(Milk.mro())
