import json


class Person:
    def __init__(self, age: int, weight: int, fat: int):
        self.age = age
        self.weight = weight
        self.fat = fat

    # @property
    # def full_name(self) -> str:
    #     return self.name

    # def __str__(self):
    #     ...
    #
    # def __repr__(self):
    #     return str(self)
    #
    # def __eq__(self, other):
    #     ...


def a():
    b = 21
    c = 80
    d = 50
    p = Person(age=b, weight=c, fat=d)
    return p

    # return b, c, d
    # return {"b": b, "c": c}
    # return {"age": b, "weight": c, "fat": d}


def main():
    result: Person = a()
    # age, weight = a()
    print(result)
    # print("fat:", result.get("fat"))
    print("fat:", result.fat)
    print("weight:", result.weight)

    # deserialization
    print(json.loads('{"spam": "eggs", "value": null, "key": false}'))
    # serialization
    print(json.dumps({'spam': 'eggs', 'value': None, 'key': False}))


if __name__ == '__main__':
    main()
