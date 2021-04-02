from food import Food

class Bear:
    def __init__(self, name, age, food):
        self.name = name
        self.age = age
        self.food = food

    def __str__(self):
        return f'{self.name}, age = {self.age}, food = {self.food}'


if __name__=='__main__':
    pear = Food('Pear', 'Fruit')
    bear = Bear('Bear', 2, pear)
    print(bear)
