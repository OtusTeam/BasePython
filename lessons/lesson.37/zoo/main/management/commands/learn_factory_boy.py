import factory
from django.core.management.base import BaseCommand
from factory.fuzzy import FuzzyInteger

from main.models import AnimalKind, Animal


class Command(BaseCommand):

    def handle(self, *args, **options):
        class AnimalKindFactory(factory.django.DjangoModelFactory):
            class Meta:
                model = AnimalKind

            name = factory.Faker('name')

        class AnimalKindEmptyFactory(factory.django.DjangoModelFactory):
            class Meta:
                model = AnimalKind

        class AnimalKindDescFactory(AnimalKindFactory):
            name = factory.Faker('name')
            max_age = 25
            desc = 'lorem'

        # animal_kind_1 = AnimalKindFactory.create()
        # animal_kind_1 = AnimalKindEmptyFactory.build()
        # animal_kind_1 = AnimalKindFactory.create()
        # animal_kind_1 = AnimalKindFactory.build(desc='...')
        # animal_kind_1 = AnimalKindEmptyFactory.build(max_age=15)
        # animal_kind_1 = AnimalKindDescFactory.build(max_age=15)
        # print(vars(animal_kind_1))
        # animal_kinds = AnimalKindFactory.build_batch(3)
        # animal_kinds = AnimalKindFactory.create_batch(3, max_age=25)
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
