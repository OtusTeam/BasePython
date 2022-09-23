import sys
from pathlib import Path

# print(sys.path)
# sys.path.append('/home/jo/220923_python_basic/220923/code/otus')
# sys.path.append('../')
# print(__file__)
# print(Path(__file__).resolve().parent.parent)
ROOT = str(Path(__file__).resolve().parent.parent)
sys.path.append(ROOT)


from utils import calc_box_area
# from ..utils_v2 import calc_cirle_area

# print(calc_cirle_area({'r': 10}))
print(calc_box_area({'w': 15, 'h': 10}))
