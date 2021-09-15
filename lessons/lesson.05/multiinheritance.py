class Point:
    is_parent = True

    def __init__(self, x=0):
        # print('Point init called')
        self.x = x

    def who_am_i(self):
        print('I am a parent point')

    def __str__(self):
        return f'Point: x = {self.x}'


class TwoDimensionalPoint(Point):

    def __init__(self, x=0, y=0):
        # print('TwoDimensionalPoint init is called')
        super(TwoDimensionalPoint, self).__init__(x)
        self.y = y

    # def who_am_i(self):
    #     print('I am a TwoDimensionalPoint point')


class ThreeDimensionalPoint(TwoDimensionalPoint):
    is_parent = False

    def __init__(self, x=0, y=0, z=0):
        # print('ThreeDimensionalPoint init is called')
        super(ThreeDimensionalPoint, self).__init__(x, y)
        self.z = z

    # def who_am_i(self):
    #     print('I am a ThreeDimensionalPoint point')

    def __str__(self):
        return f'ThreeDimensionalPoint: x={self.x}, y={self.y}, z={self.z}'


parent = Point()
# print(parent)

point_2d = TwoDimensionalPoint(3, 4)
# print(point_2d)

point_3d = ThreeDimensionalPoint(2, 4, 6)
# print(point_3d)

parent.who_am_i()
point_2d.who_am_i()
point_3d.who_am_i()


# child.who_am_i()

# print(parent)
# print(child)

# Method Resolution Order = MRO
# print(ThreeDimensionalPoint.mro())
