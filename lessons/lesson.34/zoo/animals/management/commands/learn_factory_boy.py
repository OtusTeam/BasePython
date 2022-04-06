from django.core.management.base import BaseCommand

import factory
from factory.fuzzy import FuzzyInteger

from animals.models import AnimalKind, Animal


class Command(BaseCommand):

    def handle(self, *args, **options):
        class AnimalKindFactory(factory.django.DjangoModelFactory):
            class Meta:
                model = AnimalKind

            name = factory.Faker('name')

        # class AnimalKindDescFactory(factory.django.DjangoModelFactory):
        #     class Meta:
        #         model = AnimalKind

        class AnimalKindDescFactory(AnimalKindFactory):
            name = factory.Faker('name')
            desc = 'lorem'

        # animal_kind_1 = AnimalKindFactory.create()
        # animal_kind_1 = AnimalKindFactory.build(desc='...')
        # print(vars(animal_kind_1))
        # animal_kinds = AnimalKindFactory.build_batch(3)
        # print(animal_kinds)

        class AnimalFactory(factory.django.DjangoModelFactory):
            class Meta:
                model = Animal

            name = factory.Faker('name')
            kind = factory.SubFactory(AnimalKindDescFactory)
            age = FuzzyInteger(0, 10)

        # animal_1 = AnimalFactory.build()
        animal_1 = AnimalFactory.create()
        print(vars(animal_1))
        # print(animal_1)
