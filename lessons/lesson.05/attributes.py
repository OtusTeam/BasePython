class Point:
    class_attribute = True

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.__class__.__name__} (x = {self.x}, y = {self.y})"


print(Point.class_attribute)

point = Point(4, 6)
print(point, point.x, point.y)
print(point.class_attribute)
point.class_attribute = False
print(point.class_attribute)
print(Point.class_attribute)

point_2 = Point(3, 5)
print(point_2, point_2.x, point_2.y)
print(point_2.class_attribute)

Point.class_attribute = False
print(Point.class_attribute)
print(point_2.class_attribute)
