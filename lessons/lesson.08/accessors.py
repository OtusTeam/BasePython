class House:
    def __init__(self, price):
        self._price = price
        # _House.__price

    def get_price(self):
        return self._price

    @property
    def price(self):
        print("getter is called")
        return self._price

    @price.setter
    def price(self, new_price):
        print("setter is called")
        if new_price > 0 and isinstance(new_price, float):
            self._price = new_price
        else:
            print("Please enter a valid price")


house = House(100000)
# house._price = 140000
# print(house.get_price())
# print(house._price)

print(house.price, '\n')

house.price = 110000.0
print(house.price, '\n')

house.price = -10
print(house.price)

# house.price = 10
# print(house.price)
