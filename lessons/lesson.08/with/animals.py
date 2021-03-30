from dataclasses import dataclass, field

from food import Food


# init, repr, eq, order, unsafe_hash, frozen

@dataclass
class Bear:
    name: str
    age: int = field(repr=False)
    food: Food

    def __post_init__(self):
        if self.age < 0:
            raise Exception('Age can not be less than 0')


if __name__ == '__main__':
    honey = Food('Honey', 'Sweets')
    bear = Bear('Teddy', 5, honey)
    print(honey)
    print(bear)
