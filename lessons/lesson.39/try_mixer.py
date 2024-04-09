import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zoo.settings')

import django

django.setup()

from mixer.backend.django import mixer

# from animals.models import Animal, Kind
# animals = Animal.objects.all()
# print(animals)

# kind_1 = mixer.blend('animals.Kind')
# print(kind_1)

# animal_1 = mixer.blend('animals.Animal', kind=kind_1, age=5)
# animal_1 = mixer.blend('animals.Animal', kind__name='lion')
# print(animal_1)
# print(animal_1.age)
# print(animal_1.kind)

# food_1 = mixer.blend('animals.Food')
# print(food_1)

animals = mixer.cycle(5).blend(
    # 'animals.Animal', name=(name for name in ('Alex', 'Bob'))
    # 'animals.Animal', name=mixer.sequence(),
    # 'animals.Animal', kind=mixer.SELECT,
    # 'animals.Animal', age=mixer.RANDOM,
    'animals.Animal', age=mixer.RANDOM(*[age for age in range(1, 10)])
    # 'animals.Animal', age=mixer.RANDOM(*[1, 2, 3])
)
# print(*animals, sep='\n')
for animal in animals:
    print(animal, animal.kind, animal.age)
