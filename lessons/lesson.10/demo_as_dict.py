def get_person():
    return {
        "name": "John",
        "age": 25,
        "email": "john@example.com",
    }


def update_person(person: dict):
    person["email"] = person["email"].lower()


def main():
    print("Hello!")
    person = get_person()
    print(person)
    print("name:", person["name"])
    print("age:", person["age"])
    print("email:", person["email"])


if __name__ == "__main__":
    main()
