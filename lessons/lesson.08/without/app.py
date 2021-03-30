from animals import Bear
from food import Food
from zoo import Zoo

if __name__ == '__main__':
    honey = Food('Honey', 'Sweets')
    teddy = Bear('Teddy', 2, honey)
    print(teddy)
    zoo = Zoo([])
    zoo.animals.append(teddy)
    print(zoo)
