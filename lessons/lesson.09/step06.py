class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        if isinstance(other, Product):
            return self.name == other.name and self.price == other.price
        else:
            return False

    def __lt__(self, other):
        return self.price < other.price

    def __le__(self, other):
        return self.price <= other.price

    def __gt__(self, other):
        return self.price > other.price

    def __ge__(self, other):
        return self.price >= other.price

p1 = Product('Яблоко', 100)
p2 = Product('Яблоко', 150)
p3 = Product('Яблоко', 100)


# print(p1 == p2)
# print(p1.__eq__(p2))

# print(p1 == p3)
# print(p2 == p3)
# print(p2 == p3 == p1)

print(p1 < p2)
print(p2 < p3)
print(p1 < p3)