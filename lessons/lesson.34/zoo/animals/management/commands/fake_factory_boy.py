import factory
from django.core.management.base import BaseCommand
from factory.fuzzy import FuzzyInteger

from animals.models import AnimalKind, Animal


def step_1():
    class AnimalKindFactory(factory.django.DjangoModelFactory):
        class Meta:
            model = AnimalKind

        name = factory.Faker('name')
        # is_active = False

    class NotActiveAnimalKindFactory(AnimalKindFactory):
        is_active = False

    # new_animal_kind = AnimalKind()
    # new_animal_kind.save()
    # new_animal_kind = AnimalKindFactory.create()
    # new_animal_kind = AnimalKindFactory.create(is_active=False)
    # new_animal_kind = AnimalKindFactory.build()
    new_animal_kind = NotActiveAnimalKindFactory.create()
    print(vars(new_animal_kind))


def step_2():
    class AnimalKindFactory(factory.django.DjangoModelFactory):
        class Meta:
            model = AnimalKind

        name = factory.Faker('name')

    new_animal_kinds = AnimalKindFactory.create_batch(2)
    print(new_animal_kinds)


def step_3():
    class AnimalKindFactory(factory.django.DjangoModelFactory):
        class Meta:
            model = AnimalKind

        name = factory.Faker('name')

    class AnimalFactory(factory.django.DjangoModelFactory):
        class Meta:
            model = Animal

        name = factory.Faker('name')
        kind = factory.SubFactory(AnimalKindFactory)
        age = FuzzyInteger(1, 7)

    # new_animal = AnimalFactory.build()
    new_animal = AnimalFactory.create()
    print(vars(new_animal))
    print(new_animal.kind)


def step_4():
    class AnimalKindFactory(factory.django.DjangoModelFactory):
        class Meta:
            model = AnimalKind

        name = factory.Faker('name')

    class AnimalFactory(factory.django.DjangoModelFactory):
        class Meta:
            model = Animal

        name = factory.Iterator(['Alice', 'Bob'])
        kind = factory.SubFactory(AnimalKindFactory)
        age = FuzzyInteger(1, 7)

    new_animals = AnimalFactory.build_batch(5)
    print(*map(vars, new_animals))


class Command(BaseCommand):

    def handle(self, *args, **options):
        # step_1()
        # step_2()
        # step_3()
        step_4()
