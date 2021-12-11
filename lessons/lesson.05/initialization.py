class Point:
    class_attribute = True

    # dunder, double underscore, magic
    def __init__(self, x, y, z=0):
        print("__init__ is called")
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"{self.__class__.__name__} : (x = {self.x}, y = {self.y}, z = {self.z})"


point = Point(5, 10)
print(point)

new_point = Point(4, 5, 14)
print(new_point)
print(new_point.class_attribute)

print(Point.class_attribute)
