from django.core.management.base import BaseCommand

from animals.models import AnimalKind, Animal

import factory


class Command(BaseCommand):
    def handle(self, *args, **options):
        AnimalKind.objects.all().delete()
        Animal.objects.all().delete()

        class AnimalKindFactory(factory.django.DjangoModelFactory):
            class Meta:
                model = AnimalKind

            name = factory.Faker('name')
            desc = factory.Faker('paragraph')

        class YongAnimalFactory(factory.django.DjangoModelFactory):
            class Meta:
                model = Animal

            name = factory.Faker('name')
            kind = factory.SubFactory(AnimalKindFactory)
            age = 3

        # animal_kind_1 = AnimalKindFactory.create()
        # animal_kind_1 = AnimalKindFactory.create(name='lion')
        # print(vars(animal_kind_1))

        # animal_1 = YongAnimalFactory.create()
        # animal_1 = YongAnimalFactory()
        # animal_1 = YongAnimalFactory.build()
        # print(vars(animal_1))

        animals = YongAnimalFactory.build_batch(3)
        print([vars(el) for el in animals])

        animal_kinds = AnimalKind.objects.all()
        animals = Animal.objects.all()
        print(f'AnimalKinds: {animal_kinds}')
        print(f'Animals: {animals}')
