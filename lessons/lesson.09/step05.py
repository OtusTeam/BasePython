class Cart:
    def __init__(self, items):
        self.items = items

    def __bool__(self):
        return len(self.items) > 0


cart_1 = Cart(['Ноутбук', 'Мышь'])

cart_2 = Cart([])


if cart_1:
    print('В корзине 1 есть товары')
else:
    print('В корзине 1 нет товаров')

if cart_2:
    print('В корзине 2 есть товары')
else:
    print('В корзине 2 нет товаров')