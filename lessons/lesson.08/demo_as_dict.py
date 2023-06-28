class Person:
    def __init__(self, name, age, email):
        self.name = name
        ...

    def __eq__(self, other):
        return False

    def __str__(self):
        return ""

    def __repr__(self):
        return str(self)


def get_person():
    return {
        "name": "John",
        "age": 42,
    }


def main():
    person = get_person()
    print(person)
    print(person["name"])
    # print(person["nmae"])
    person_2 = get_person()
    person_2["name"] = "Sam"
    person_2["email"] = "email@example.com"
    print(person_2)
    print(person_2["email"])
    print(person["email"])



if __name__ == '__main__':
    main()
