class Point:
    """
    + init
    + repr
    + eq
    order
    unsafe_hash
    frozen
    match_args
    kw_only
    slots
    weakref_slot
    """
    __slots__ = ("x", "y", "z")

    def __init__(self, x: int, y: int, z: int = 0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"{self.__class__.__name__}(x={self.x!r}, y={self.y!r}, z={self.z!r})"

    def __repr__(self):
        return str(self)

    def __eq__(self, other: "Point"):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y and self.z == other.z


def get_person():
    # pass
    # return
    # return None
    return {
        "name": "John",
        "age": 42,
        # "email": None,
    }


def main():
    person = get_person()
    print(person)
    print(person["name"])
    # print(person["email"])
    print(person["age"])

    person_2 = get_person()
    person_2["name"] = "Sam"
    person_2["age"] = 22
    print(person_2)
    person_2["email"] = "sam@example.com"
    print(person_2)
    print(person_2["email"])
    # print(person["email"])


if __name__ == "__main__":
    main()
