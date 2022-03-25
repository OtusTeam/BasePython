# from math import pi
import math

# from utils import (
#     box_area, circle_area,
#     triangle_area
# )
import utils

a, b = 5, 2
area_1 = utils.box_area(a, b)

r_1 = 4.5
area_2 = utils.circle_area(r_1)

b_1, h_1 = 7, 3
area_3 = utils.triangle_area(b_1, h_1)

print(area_1, area_2, area_3)
print(math.pi)
