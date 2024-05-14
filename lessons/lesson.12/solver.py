class Solver:
    TYPE_ERROR_TEXT = "Operands should be of one type"

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        try:
            res = self.a + self.b
        except TypeError:
            raise TypeError(self.TYPE_ERROR_TEXT)
        return res

    def mul(self):
        return self.a * self.b

    def clear(self):
        # какая-то полезная пост-работа, очистка и тд
        print("clear solver", self)
