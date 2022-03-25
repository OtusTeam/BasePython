import math
# import xgboost

# import numpy as np
# import pandas as pd

import utils as ut

a, b = 5, 2
area_1 = ut.box_area(a, b)

r_1 = 4.5
area_2 = ut.circle_area(r_1)

b_1, h_1 = 7, 3
area_3 = ut.triangle_area(b_1, h_1)

print(area_1, area_2, area_3)
print(math.pi)
