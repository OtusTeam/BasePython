def get_person():
    return {
        "name": "John",
        "age": 42,
        "email": "john@example.com",
    }


def main():
    person = get_person()
    print("name:", person["name"])
    print("age:", person["age"])
    print("email:", person["email"])


if __name__ == "__main__":
    main()
