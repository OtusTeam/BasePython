class Student:
    is_annoyed = True

    def __init__(self, name, surname, faculty, year):
        self.name = name
        self.surname = surname
        self.faculty = faculty
        self.year = year


student = Student('Nigar', 'Movsumova', 'Computer Sciences', 2)
print(student.name)
print(student.is_annoyed)
print(Student.is_annoyed)
# print(Student.name)
