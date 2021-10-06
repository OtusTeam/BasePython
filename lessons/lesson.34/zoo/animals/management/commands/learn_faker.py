from django.core.management.base import BaseCommand
from faker import Faker
from faker_music import MusicProvider

from animals.models import AnimalKind


class Command(BaseCommand):
    def handle(self, *args, **options):
        # def get_faker(locale='en_US'):
        #     return Faker(locale=locale)

        # faker = Faker(['ru_RU', 'es_ES'])
        # faker = Faker()
        faker = Faker('ru_RU')
        faker.add_provider(MusicProvider)
        word_list = ['python', 'урок', 'разработка']

        # for _ in range(2):
        #     # print(faker.first_name())
        #     # print(faker.last_name())
        #     # print(faker.address())
        #     # print(faker.music_genre_object())
        #     print(faker.sentence(ext_word_list=word_list))

        knimal_kind_1 = AnimalKind.objects.create(
            name=faker.name(),
            desc=faker.paragraph()
        )
        print(vars(knimal_kind_1))
