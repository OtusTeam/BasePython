class Point:
    is_parent = True

    def __init__(self, x=0):
        self.x = x

    def who_am_i(self):
        print('I am a 1d point')

    def __str__(self):
        return f'Point: x = {self.x}'


class TwoDimensionalPoint(Point):

    def __init__(self, x=0, y=0):
        # print('TwoDimensionalPoint init is called')
        # Point.__init__(self, x)
        self.y = y
        super(TwoDimensionalPoint, self).__init__(x)

    # def who_am_i(self):
    #     print('I am a 2d point')

    def __str__(self):
        return f'TwoDimensionalPoint: x = {self.x}, y = {self.y}'


class ThreeDimensionalPoint(TwoDimensionalPoint):
    is_parent = False

    def __init__(self, x=0, y=0, z=0):
        # print('ThreeDimensionalPoint init is called')
        super(ThreeDimensionalPoint, self).__init__(x, y)
        self.z = z

    # def who_am_i(self):
    #     print('I am a 3d point')

    def __str__(self):
        return f'ThreeDimensionalPoint: x={self.x}, y={self.y}, z={self.z}'


parent = Point()
print(parent)

point_2d = TwoDimensionalPoint()
print(point_2d)

point_3d = ThreeDimensionalPoint()
print(point_3d)

parent.who_am_i()
point_2d.who_am_i()
point_3d.who_am_i()

# Point.who_am_i(point_3d)


# child.who_am_i()

# print(parent)
# print(child)

# Method Resolution Order = MRO
# print(ThreeDimensionalPoint.mro())
