from .base import pi


def calc_cirle_area(circle):
    return pi * circle['r'] ** 2


def calc_box_area(box):
    return box['w'] * box['h']
