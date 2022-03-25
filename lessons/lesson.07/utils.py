# from math import pi
pi = 3.1416


def box_area(a, b):
    return a * b


def circle_area(r):
    return pi * r ** 2


def triangle_area(b, h):
    return b * h / 2


if __name__ == '__main__':
    print(globals())
    print(__name__)
    print(__file__)
    print(box_area(2, 3))
    print(circle_area(1))
