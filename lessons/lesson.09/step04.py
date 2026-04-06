class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        return f'{self.name} выполняет рабочую задачу'

    def __str__(self):
        return f'{self.name} выполняет рабочую задачу!'


class Manager(Employee):
    def work(self):
        return f'{self.name} управляет командой'

    def __str__(self):
        return f'{self.name} управляет командой!'

e = Employee('Bob', 20)
m = Manager('Alice', 30)
# print(e.work())
# print(m.work())
print(e)
print(m)