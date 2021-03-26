
# 1. импортирование всего модуля
# import baskets
# 2. импортирование модуля с псевдонимом
# import basket as bskt

# 3. импортирование только того, что юзаем
from baskets import Basket, PriceValueError

# 4. импорт всего - bad practise - импортировать можем лишнее + нечитабельно + конфликт имен
# from baskets import *

print(__name__)

if __name__ == '__main__':
    basket = Basket()
    print(basket)
