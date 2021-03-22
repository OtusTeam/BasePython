class Basket:
    def __init__(self):
        self.items = ['apple', 'banana']
        self.count = {'apple': 10, 'banana': 5}

    def __getitem__(self, key):
        return self.count[key]


basket = Basket()
print(basket.count)
