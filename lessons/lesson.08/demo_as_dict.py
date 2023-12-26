def get_person():
    return {
        "name": "John",
        "age": 42,
        "email": None,
    }


def main():
    person = get_person()
    print(person)
    name = person["name"]
    print("name:", name)
    age = person["age"]
    print("age:", age)

    person_2 = get_person()
    person_2["username"] = "Sam"
    person_2["age"] = 22
    person_2["email"] = "sam@example.com"

    print(person_2)

    name = person_2["name"]
    print("name:", name)


if __name__ == "__main__":
    main()
