from django.core.management.base import BaseCommand
from faker import Faker
from animals.models import Family
from faker_music import MusicProvider


class Command(BaseCommand):

    def handle(self, *args, **options):
        fake = Faker('ru-ru')
        print(fake.name())
        print(fake.address())
        print(fake.text())
        print('-'*20)
        print(fake.rgb_color())
        print(fake.color(hue='red', color_format='rgb'))
        fake.add_provider(MusicProvider)
        print(fake.music_genre_object())

        family = Family.objects.create(name=fake.name())
        print(family.name)
        family.delete()