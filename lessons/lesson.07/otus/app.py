# from utils import *
from utils import (
    calc_cirle_area, calc_box_area,
    calc_triangle_area, calc_penta_area,
)
# from utils.simple import calc_cirle_area, calc_box_area
# from utils.complicated import calc_triangle_area, calc_penta_area


def main():
    # print(globals())

    circle_1 = {
        'r': 5
    }
    circle_1['area'] = calc_cirle_area(circle_1)
    print(circle_1['area'])

    circle_2 = {
        'r': 15
    }
    circle_2['area'] = calc_cirle_area(circle_2)
    print(circle_2['area'])

    box_1 = {
        'w': 10,
        'h': 15,
    }
    box_1['area'] = calc_box_area(box_1)
    print(box_1['area'])

    print(max([circle_1['area'], circle_2['area'], box_1['area']]))


if __name__ == '__main__':
    main()
