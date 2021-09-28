class Solver:
    EXC_TYPE_ERROR_TEXT = "a and b have to be int or float"

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def mul(self):
        if not (
            isinstance(self.a, (int, float))
            and isinstance(self.b, (int, float))
        ):
            raise TypeError(self.EXC_TYPE_ERROR_TEXT)
        return self.a * self.b


def add(a, b):
    return a + b
