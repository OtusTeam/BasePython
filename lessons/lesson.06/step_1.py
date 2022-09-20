def add(a, b):
    return a + b


print(add(1, 2))
print(add(1, 10))


# c = add(1, "0")
# c = add(2, 8)

# print(c / 2)

print([1, 2] + [3])


class mylist(list):
    def __add__(self, other):
        if isinstance(other, int):
            other = [other]
        return super().__add__(other)


print(mylist((1, 2)) + 3)
print(mylist((1, 2)) + [3, 4])


# raise print("asdasd", "sdfsdf", Exception)
raise NameError("неправильное имя")
raise Exception("ты неправ... (потому что...)")
print("never")

