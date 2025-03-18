class Select:
    def __init__(self, name, *filters):
        self.name = name
        self.filters = filters

    def where(self, *filters):
        return Select(
            self.name,
            *self.filters,
            *filters,
        )


def main():
    stmt = Select("qwerty").where("foo", "bar", 1 == 2).where()
    print(stmt.name)
    print(stmt.filters)
    stmt = stmt.where("spam", "eggs", False == 0)
    print(stmt.filters)

    print(dict(foo="bar").items())

    res = "sadfasdfgrhSD".upper().replace("A", "_").replace("D", "-")
    print(res)


if __name__ == "__main__":
    main()
