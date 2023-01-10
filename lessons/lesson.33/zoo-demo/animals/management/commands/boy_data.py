from mixer.backend.django import mixer
from django.core.management.base import BaseCommand, CommandError
from animals.models import Animal, Category, Card, Food
from faker import Faker
from faker_music import MusicProvider
from animals.factorys import CategoryFactory, AnimalFactory


class Command(BaseCommand):
    help = 'Factory boy data'

    def handle(self, *args, **options):
        print('Make data')
        Card.objects.all().delete()
        Animal.objects.all().delete()
        Category.objects.all().delete()

        category = CategoryFactory.create()
        print(category.name)
        print(category.id)

        category = CategoryFactory.create(name='Tiger')
        print(category.name)
        print(category.id)

        category = CategoryFactory.build()
        print(category.name)
        print(category.id)

        animal = AnimalFactory.build()
        print(animal.category.name)
        print(animal.name)