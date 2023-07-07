class Solver:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def mul(self):
        res = self.a * self.b
        print(res)
        return res
