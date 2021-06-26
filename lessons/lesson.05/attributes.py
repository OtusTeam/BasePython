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
