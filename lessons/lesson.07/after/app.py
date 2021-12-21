# 1. импортирование всего модуля
# import baskets
# import new_baskets

# 2. импортирование модуля с псевдонимом
# import baskets as bskt
# import numpy as np
# import pandas as pd


# 3. import basket
from baskets import Basket, IncorrectValueNumber, test_function, RELATIVE_PATH, DIRECTORY, DIRECTORY


# 4. импорт всего из модуля - импортирование лишнего, конфликты, нечитабельно
# from baskets import *
# from basket.main import Basket

# def print_path():
#     # import baskets
#     from baskets import DIRECTORY
#     print(DIRECTORY)
# from basket.main import Basket

if __name__ == '__main__':
    basket = Basket()
    print(basket)
    print(DIRECTORY())
    # main_basket = Basket()
    # print(main_basket)
    # my_basket = baskets.Basket()
    # print(baskets)
    # basket = bskt.Basket()
    # print(basket)
    # baskets.test_function()
    # import baskets
    print(DIRECTORY)
    print(RELATIVE_PATH)
    test_function()

    # new_basket = new_baskets.Basket()
    # print(new_basket)
    # raise IncorrectValueNumber()
    # print_path()
