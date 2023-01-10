from mixer.backend.django import mixer
from django.core.management.base import BaseCommand, CommandError
from animals.models import Animal, Category, Card, Food
from faker import Faker
from faker_music import MusicProvider


class Command(BaseCommand):
    help = 'Mixer data'

    def handle(self, *args, **options):
        Card.objects.all().delete()
        Animal.objects.all().delete()
        Category.objects.all().delete()
        # императивность (декларативность)
        # он всегда сохраняет в базу
        card = mixer.blend(Card)
        print(card.text)
        print(card.animal.name)
        print(card.animal.category.name)

        food = mixer.blend(Food)
        print(food.animals.all())

        card = mixer.blend(Card, text='BBB')
        print(card.text)

        card = mixer.blend(Card, animal__name='Parrot')
        print(card.animal.name)

        card = mixer.blend(Card, animal__category__name='Parrot')
        print(card.animal.category.name)

        mixer.cycle(3).blend(Category, name=(name for name in ('One', 'Two', 'Three')))

        categories = mixer.cycle(3).blend(Category, name=mixer.sequence(lambda number: "test_%s" % number))

        print(categories)
        print(type(categories))

        animal = mixer.blend(Animal)
        print(animal.age)

        animal = mixer.blend(Animal, category=mixer.SELECT)
        print(animal.category.name)
        print(Category.objects.all())

        animal = mixer.blend(Animal, age=mixer.RANDOM, category__code=mixer.RANDOM)
        print(animal.age)
        print(animal.category.code)

        mixer.cycle(100).blend(Animal)







