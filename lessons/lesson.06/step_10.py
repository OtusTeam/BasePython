class Vector:
    def __init__(self, *items):
        self.items = items

    def __add__(self, other):
        new_items = [one + two for one, two in zip(self.items, other.items)]
        return self.__class__(*new_items)

    def __iadd__(self, other):
        self.items = tuple([one + two for one, two in zip(self.items, other.items)])
        return self


v_1 = Vector(1, 2, 3)
v_2 = Vector(5, 6, 7)
# v_3 += v_1 + v_2 + v_1
print(id(v_2))
v_2 += v_1
# print(v_3.items)
print(v_2.items)
print(id(v_2))
var_3 = []
print(dir(var_3))
print(5 in var_3)
