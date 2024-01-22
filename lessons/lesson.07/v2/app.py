import math
import random

# import numpy as np
# import pandas as pd

import products as pr
import users as usr


def main():
    usr.create('Ivan')
    usr.update('Ivan', age=28)

    pr.create('iphone')
    pr.update('iphone', price=1000)


main()
