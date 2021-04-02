from dataclasses import dataclass


# класс становится неизменяемым
@dataclass(frozen=True)
# @dataclass
class Food:
    name: str
    food_type: str

    # def __init__(self, name, food_type, taste):
    #     self.name = name
    #     self.food_type = food_type
    #     self.taste = taste


# @dataclass
# class Test(Food):
#     test: str


if __name__ == '__main__':
    honey1 = Food('Honey', 'Sweets')
    honey2 = Food('Honey', 'Sweets')
    # honey1 = Food('Honey', 'Sweets', 'Tasty')
    # honey2 = Food('Honey', 'Sweets', 'Awful')
    print(honey1)
    print(honey2)
    print(honey1 == honey2)
    # print(honey1.taste)
    # при frozen = True выдаст ошибку
    # honey1.taste = None
    # honey1.name = 'Test'
    # test = Test('Food Test', 'Test Food', 'Test')
    # print(test)

