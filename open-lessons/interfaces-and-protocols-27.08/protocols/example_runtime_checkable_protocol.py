from typing import Protocol, runtime_checkable


@runtime_checkable
class Draggable(Protocol):
    weight: int
    handles: int


class Bag:
    def __init__(self, weight: int, handles: int = 2) -> None:
        self.weight = weight
        self.handles = handles


class SuitCase:
    def __init__(self, weight: int, handles: int = 1) -> None:
        self.weight = weight
        self.handles = handles


class Cat:
    def __init__(self, name: str, weight: int) -> None:
        self.name = name
        self.weight = weight


def drag(item: Draggable) -> None:
    print("Drag", item.weight, "kg using", item.handles, "handles")


def main():
    bag = Bag(15)
    case = SuitCase(7)
    cat = Cat("Cat", 5)
    elements = [bag, case, cat]
    for el in elements:
        if isinstance(el, Draggable):
            drag(el)
        else:
            print(el, "is not draggable")


if __name__ == "__main__":
    main()
