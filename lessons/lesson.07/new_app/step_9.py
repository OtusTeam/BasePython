# import os, sys
import os
import sys

# import numpy as np

# sys.path.append('/home/jo/220318_basics/220325/code')
# ROOT = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(__file__)
sys.path.append(os.path.join(ROOT, '../'))

from utils import box_area

a, b = 5, 2
area_1 = box_area(a, b)
print(area_1)
