from dataclasses import dataclass


# класс становится неизменяемым
@dataclass(frozen=True)
class Food:
    name: str
    food_type: str


if __name__ == '__main__':
    honey1 = Food('Honey', 'Sweets')
    honey2 = Food('Honey', 'Sweets')
    print(honey1 == honey2)
