from pydantic import BaseModel, Extra


class Point(BaseModel):
    x: int
    y: int


class Person(BaseModel):
    age: int
    weight: int
    email: str = None
    # name: str = None
    # spam: str = None

    def increase_age(self):
        self.age += 1
        return self.age

    class Config:
        # frozen = True
        frozen = False
        extra = Extra.ignore
        # extra = Extra.allow


def get_point():
    return Point(x=20, y=70)


def get_person():
    return Person(age=20, weight=70, foo="bar", spam="eggs")


def main():
    p1 = get_point()
    print(p1)
    print(repr(p1))
    person_1 = get_person()
    print(person_1)
    print(repr(person_1))
    person_1.email = "asd"
    # print(person_1.spam)
    print(person_1.dict())
    person_1.increase_age()
    print(person_1)


if __name__ == "__main__":
    main()
