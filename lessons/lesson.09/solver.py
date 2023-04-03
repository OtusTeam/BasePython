class Solver:
    """
    >>> s = Solver(2, 3)
    >>> s.add()
    5
    """

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        # return sum([self.a, self.b])
        result = self.a + self.b
        # print(result)
        return result

    def mul(self):
        return self.a * self.b
