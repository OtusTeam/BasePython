
class Solver:
    PARAMS_TYPE_EXC_TEXT = "values should be nums!"
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        # return
        # return 5
        return self.a + self.b
        # return 7
        # return 3

    def mul(self):
        if not (
            isinstance(self.a, (int, float))
            and isinstance(self.b, (int, float))
        ):
        # if not all((
        # # if not any((
        #     isinstance(self.a, (int, float)),
        #     isinstance(self.b, (int, float)),
        # )):
            raise TypeError(self.PARAMS_TYPE_EXC_TEXT)
        return self.a * self.b
        # return self.a + self.b


def div(a, b):
    return a / b
