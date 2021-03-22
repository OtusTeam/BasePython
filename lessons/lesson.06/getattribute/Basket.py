class Basket:
    def __init__(self):
        self.items = ['apple', 'banana']

    # getattribute вызывается при каждом вызове метода или аттрибута через объект
    def __getattribute__(self, items):
        print('get attribute method is called')
        return super().__getattribute__(items)


basket = Basket()
print(basket.items)
