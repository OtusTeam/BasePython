class Solver:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        # return self.a + self.b
        res = self.a + self.b
        print("res:", res)
        # return
        return res

    def mul(self):
        return self.a * self.b
