class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def make_discount(self, discount):
        """discount: in percents"""
        self.price *= (100 - discount) / 100

    # def make_discount_2(self, price, discount):
    #     price *= (100 - discount) / 100
    #     return price

    def to_html(self):
        return f'<h1>{self.name} <b>{self.price}</b></h1>'


prod_1 = Product('iPhone', 1988.64)
print(prod_1)
print(prod_1.name)
print(prod_1.price)
prod_1.make_discount(5)
print(prod_1.price)
print(prod_1.to_html())


b = 25


def make_discount(obj, discount):
    # global b
    b = 15
    print(b)
    obj.price *= (100 - discount) / 100


print(b)
#
#
# make_discount(prod_1, 5)
# # make_discount(prod_5, 5)
# print(prod_1.price)
