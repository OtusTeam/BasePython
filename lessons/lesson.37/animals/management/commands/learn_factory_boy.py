import factory
from django.core.management.base import BaseCommand
from factory.fuzzy import FuzzyInteger

from animals.models import Category, Animal


class Command(BaseCommand):

    def handle(self, *args, **options):
        class AnimalCategoryEmptyFactory(factory.django.DjangoModelFactory):
            class Meta:
                model = Category

        class AnimalCategoryFactory(AnimalCategoryEmptyFactory):
            name = factory.Faker('name')

        class AnimalCategoryDescFactory(AnimalCategoryFactory):
            desc = 'lorem'


        # animal_kind_1 = AnimalCategoryEmptyFactory.create()
        # print(animal_kind_1, animal_kind_1.pk)
        # animal_kind_1 = AnimalCategoryEmptyFactory.build()
        # print(animal_kind_1, animal_kind_1.pk)
        # animal_kind = AnimalCategoryFactory.create()
        # print(animal_kind, animal_kind.pk)
        # animal_kind = AnimalCategoryFactory.create(desc='some')
        # print(animal_kind, animal_kind.pk)
        animal_kind = AnimalCategoryDescFactory.create()
        print(animal_kind, animal_kind.pk)

        # animal_kinds = AnimalCategoryDescFactory.build_batch(3)
        animal_kinds = AnimalCategoryDescFactory.create_batch(3)
        print(animal_kinds)

        class AnimalFactory(factory.django.DjangoModelFactory):
            class Meta:
                model = Animal

            name = factory.Faker('name')
            category = factory.SubFactory(AnimalCategoryFactory)
            age = FuzzyInteger(1, 10)

        # animal_1 = AnimalFactory.build()
        animal_1 = AnimalFactory.create()
        print(vars(animal_1))
