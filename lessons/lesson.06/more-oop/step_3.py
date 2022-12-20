class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def make_discount(self, discount):
        """discount: in percents"""
        self.price *= (100 - discount) / 100

    def to_html(self):
        return f'<h1>{self.name} <b>{self.price}</b></h1>'


# def vars(obj):
#     return obj.__dict__


prod_1 = Product('iPhone', 1988.64)
prod_2 = Product('MacBook', 2507.77)
print(vars(prod_1))
print(vars(prod_2))
# print(prod_1.__dict__)
