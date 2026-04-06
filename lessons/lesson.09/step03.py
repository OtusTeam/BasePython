
class Student:
    def __init__(self, name, age=20):
        self.name = name
        self.age = age

    def show_info(self):
        return 'Это объект студента'

    def __str__(self):
        return f'Студент {self.name}, {self.age} лет'

    def __repr__(self):
        return f"Student('{self.name}')"


student1 = Student(name='Bob', age=18)
print(student1)
# # print(student.__str__())
# # print(student.show_info())
student2 = Student('Ivan')
# student3 = Student('Anna')
#
# s_list = [student1, student2, student3]
# print(s_list)
#
# for s in s_list:
#     print(s)
#     print(repr(s))