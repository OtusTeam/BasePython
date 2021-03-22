class Basket:
    def __init__(self):
        self.items = ['apple', 'banana']
        self.count = {}

    def __setitem__(self, key, value):
        self.count[key] = value


banana_count = 10
basket = Basket()
basket['banana'] = banana_count
#apple_count = 10
#basket['apple'] = apple_count
print(basket.count)
