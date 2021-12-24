from random import choice, randint, sample

from django.core.management.base import BaseCommand

from animals.models import AnimalKind, Animal, AnimalFood


class Command(BaseCommand):

    def handle(self, *args, **options):
        animal_kinds = ['lion', 'monkey', 'parrot', 'elephant', 'cat']
        animal_kinds_obj = []
        for animal_kind in animal_kinds:
            # animal_kinds_obj[animal_kind] = AnimalKind.objects.create(name=animal_kind)
            _obj, created = AnimalKind.objects.get_or_create(name=animal_kind)
            animal_kinds_obj.append(_obj)

        animals = ['Bob', 'Alice', 'Tom', 'Jerry']
        animals_obj = []
        for animal in animals:
            _obj = Animal.objects.create(name=animal,
                                         kind=choice(animal_kinds_obj),
                                         age=randint(1, 10))
            animals_obj.append(_obj)

        food_items = ['meet', 'egg', 'banana', 'apple', 'water']
        food_obj = []
        for food in food_items:
            _obj, created = AnimalFood.objects.get_or_create(name=food)
            food_obj.append(_obj)

        for food in food_obj:
            animals = sample(animals_obj, k=randint(1, len(animals_obj)))
            for animal in animals:
                food.animal.add(animal)
            food.save()

