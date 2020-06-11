class Person:
    WHAT_TO_SAY_PERSON = "My name is {name} and I'm {age} years old"

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def say(self):
        speech = self.WHAT_TO_SAY_PERSON.format(name=self.name, age=self.age)
        print(speech)
        return speech


class Employee(Person):
    WHAT_TO_SAY_EMPLOYEE = "I work {years} years already and get {salary} annually"

    def __init__(self, name: str, age: int, salary: int, experience: int):
        super().__init__(name, age)
        self.salary = salary
        self.experience = experience

    def say(self):
        initial_speech = super().say()
        speech = "\n".join((
            initial_speech,
            self.WHAT_TO_SAY_EMPLOYEE.format(years=self.experience, salary=self.salary)
        ))
        print(speech)
        return speech


if __name__ == '__main__':
    employee = Employee("John", 30, 100_000, 7)
    employee.say()
