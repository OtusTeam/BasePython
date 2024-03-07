def get_person():
    return {
        "name": "John Smith",
        "age": 42,
        "email": None,
    }


def main():
    p = get_person()
    print(p)
    print("name:", p["name"])
    print("email:", p["email"])
    print("age:", p["age"])


if __name__ == "__main__":
    main()
