import random


class Solver:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def mul(self):
        return self.a * self.b

    def add_random_value(self):
        random_value = random.randint(1, 100)
        print(random_value)
        return self.add() + random_value



def dev(a, b):
    return a/b


if __name__ == '__main__':
    # solver = Solver(1, 2)
    # print(solver.add()) # тут должно быть 3

    solver = Solver(1, 2)
    result = solver.add()
    assert solver.add() == 3, f'{result} != 3'

    solver = Solver(3, 5)
    assert solver.add() == 8

    solver = Solver(1, 2)
    print(solver.add_random_value())