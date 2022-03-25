from math import pi

from utils import box_area, circle_area, triangle_area
# from utils import *  # NEVER

a, b = 5, 2
area_1 = box_area(a, b)

r_1 = 4.5
area_2 = circle_area(r_1)

b_1, h_1 = 7, 3
area_3 = triangle_area(b_1, h_1)

print(area_1, area_2, area_3)
print(pi)
