class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __len__(self):
        # i = 0
        # for c in self.name:
        #     i += 1
        # return i
        # return len(self.name)
        return self.age


p1 = Person("John", 10)
p2 = Person("Sam", 12)

print(p1.name, len(p1))
print(p2.name, len(p2))


