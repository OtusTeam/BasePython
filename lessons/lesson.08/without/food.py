class Food:
    def __init__(self, name, food_type):
        self.name = name
        self.food_type = food_type

if __name__=='__main__':
    honey1 = Food('Honey', 'Sweets')
    honey2 = Food('Honey', 'Sweets')
    print(honey1 == honey2)