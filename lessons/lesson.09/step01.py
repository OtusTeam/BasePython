# print(obj)
# obl.__str__()
#
# obj1 + obj2   obj1.__add__(obj2)


class Student:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        return 'Это объект студента'

    def __str__(self):
        return f'Студент {self.name}'

    def __repr__(self):
        return f"Student('{self.name}')"


student1 = Student('Bob')
# print(student)
# print(student.__str__())
# print(student.show_info())
student2 = Student('Ivan')
student3 = Student('Anna')

s_list = [student1, student2, student3]
print(s_list)

for s in s_list:
    print(s)
    print(repr(s))