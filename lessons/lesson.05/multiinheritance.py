class Human:
    def __init__(self, name, birth_date, weight, height, sex, location):
        self.name = name
        self.birth_date = birth_date
        self.weight = weight
        self.height = height
        self.sex = sex
        self.location = location

    def eat(self):
        print("I can eat")

    def breathe(self):
        print("I can breathe")

    def __str__(self):
        return f"{self.__class__.__name__} : "


class Employee:

    def __init__(self, position, salary, experience, start_date):
        self.position = position
        self.salary = salary
        self.start_date = start_date
        self.experience = experience


    def work(self):
        print("I can work")

    def __str__(self):
        return f"{self.__class__.__name__} : ( position = {self.position}," \
               f" salary = {self.salary}, experience = {self.experience}," \
               f" start_date = {self.start_date})"


class Manager(Employee, Human):
    pass


manager = Manager("Sales Manager", 4000, 3, '01-12-2021')
print(manager)
manager.work()
manager.eat()

# MRO - Method Resolution Order
print(Manager.mro())


for method_name in dir(manager.work()):
    if callable(getattr(manager.work(), method_name)):
        print(method_name)


def str_for_function(function):
    return f"hello world"


manager.work().__str__ = str_for_function(manager.work())
print(manager.work())

