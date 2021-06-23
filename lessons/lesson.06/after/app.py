# 1. импортирование всего модуля
# import basket

# 2. импортирование модуля с псевдонимом
# import basket as bskt


# 3. import basket
from basket import Basket, IncorrectValueNumber

# 4. импорт всего из модуля - импортирование лишнего, конфликты, нечитабельно
# from basket import *


if __name__ == '__main__':
    basket = Basket()
    print(basket)
