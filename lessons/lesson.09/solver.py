class Solver:

    EXC_TYPE_ERROR_TEXT = "can't multiply strings"

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        res = self.a + self.b
        print(res)
        return res
        # return self.a + self.b

    def mul(self):
        if isinstance(self.a, str) and isinstance(self.b, str):
            raise TypeError(self.EXC_TYPE_ERROR_TEXT)

        return self.a * self.b
