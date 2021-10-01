# 1. импортирование всего модуля
# import baskets
# import new_baskets

# 2. импортирование модуля с псевдонимом
# import baskets as bskt
# import numpy as np
# import pandas as pd


# 3. import basket
# from baskets import Basket, IncorrectValueNumber


# 4. импорт всего из модуля - импортирование лишнего, конфликты, нечитабельно
# from baskets import *
# from basket.main import Basket

def print_path():
    # import baskets
    from baskets import DIRECTORY
    print(DIRECTORY)


if __name__ == '__main__':
    # basket = baskets.Basket()
    # print(basket)
    # baskets.test_function()
    # import baskets
    # print(baskets.DIRECTORY)
    # print(baskets.RELATIVE_PATH)
    # new_basket = new_baskets.Basket()
    # print(new_basket)
    # raise IncorrectValueNumber()
    print_path()
