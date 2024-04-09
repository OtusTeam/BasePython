from datetime import datetime

from django.core.management.base import BaseCommand
import factory
from factory.fuzzy import FuzzyInteger

from myauth.models import OtusUser
from animals.models import Animal, Kind


class Command(BaseCommand):
    help = "Learn factory boy"

    def handle(self, *args, **options):
        class KindFactory(factory.django.DjangoModelFactory):
            class Meta:
                model = Kind

            name = factory.Faker('name')

        class AnimalFactory(factory.django.DjangoModelFactory):
            class Meta:
                model = Animal

            name = factory.Faker('name')
            kind = factory.SubFactory(KindFactory)
            age = FuzzyInteger(1, 10)
            # kind_id = 3

        # animal_1.kind_id
        # animal_1.kind
        # animal_1 = AnimalFactory.build()
        animal_1 = AnimalFactory.create(name='Abcde')
        print(vars(animal_1))

        # animals = AnimalFactory.build_batch(3)
        animals = AnimalFactory.create_batch(3)
        for animal in animals:
            print(vars(animal))
