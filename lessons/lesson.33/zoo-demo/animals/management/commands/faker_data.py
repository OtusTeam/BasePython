from django.core.management.base import BaseCommand, CommandError
from animals.models import Animal, Category, Card, Food
from faker import Faker
from faker_music import MusicProvider


class Command(BaseCommand):
    help = 'Faker data'

    def handle(self, *args, **options):
        print('Fake data')
        fake = Faker(['it_IT', 'ru_RU', 'ar_AA'])
        #fake = Faker(['ar_AA'])

        print(fake.name())
        # 'Lucy Cechtelar'

        print(fake.address())
        # '426 Jordy Lodge
        #  Cartwrightshire, SC 88120-6700'

        print(fake.text())

        print(fake.first_name())
        print(fake.last_name())

        print(fake.color(hue='orange', color_format='rgb'))

        fake = Faker()
        fake.add_provider(MusicProvider)

        print(fake.music_genre_object())

        Card.objects.all().delete()
        Animal.objects.all().delete()
        Category.objects.all().delete()
        self.category = Category.objects.create(name=fake.name())
        print(self.category.name)

        print(fake.number())