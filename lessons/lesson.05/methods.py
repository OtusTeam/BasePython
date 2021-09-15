class Point:

    # инициализатор
    # self - используемый экземпляр объекта
    def __init__(self, x, y, z):
        # x и y - это instance attributes, то есть аттрибуты экземпляра
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"{self.__class__.__name__} (x = {self.x}, y = {self.y}, z = {self.z})"

    # добавить дополнительный метод для распечатки


point = Point(4, 6, 5)

print(point, point.x, point.y)

# Magic methods are not meant to be invoked directly by you, but the invocation #happens internally from the class on a certain action. For example, when you #add two numbers using the + operator, internally, the __add__()

# https://www.tutorialsteacher.com/python/magic-methods-in-python

# Метод- это функция, прописанная внутри класса
