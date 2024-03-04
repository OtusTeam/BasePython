# products actions
def create(name):
    print(f"Created product {name=}")
    return ...


def update(name, **kwargs):
    print(f"Updated product {name=} with {kwargs=}")


def main():
    create("Tablet")
    create("Laptop")
    update("Tablet", size=10, color="red")
    update("Laptop", price=1999, category="Gaming")

    print(__file__)
    print(__name__)


if __name__ == "__main__":
    main()
