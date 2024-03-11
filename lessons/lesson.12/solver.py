class Solver:
    TYPE_ERROR_TEXT = "Operands should be of one type"

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        # res = self.a + self.b

        try:
            res = self.a + self.b
        except TypeError:
            raise TypeError(self.TYPE_ERROR_TEXT)
        print("res:", res)
        # print("10/res:", 10 / res)
        # if res == 7:
        #     1/0
        return res

    def mul(self):
        return self.a * self.b

    def delete(self):
        print("delete me", self)
