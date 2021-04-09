UNEXPECTED_TYPE = "Got unexpected type!"


def is_numeric_type(x):
    return isinstance(x, (int, float))


class Solver:
    def add(self, a, b):
        if not all(
            map(
                is_numeric_type,
                (a, b)
            )
        ):
            raise TypeError(UNEXPECTED_TYPE)

        result = a + b
        print("add", a, "and", b, "is =", result)
        return result


def mul(a, b):
    return a * b
