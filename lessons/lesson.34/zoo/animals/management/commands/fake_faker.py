import random

from django.core.management.base import BaseCommand
from faker import Faker
from faker.providers import BaseProvider
from faker_music import MusicProvider


def step_1():
    faker = Faker('ru_RU')
    # faker = Faker()
    # faker.seed_instance(15)
    # print(faker.name())
    print(faker.name())
    print(faker.first_name())
    print(faker.last_name())
    print(faker.address())
    print(faker.user_name())
    print(faker.email())


def step_2():
    faker = Faker()
    faker.add_provider(MusicProvider)

    print(faker.music_genre())
    print(faker.music_genre_object())


def step_3():
    faker = Faker()

    class FoodProvider(BaseProvider):
        def food(self):
            return random.choice(['meet', 'banana', 'water'])

    faker.add_provider(FoodProvider)

    print(faker.food())
    print(faker.food())


def step_4():
    faker = Faker()

    print(faker.sentence(ext_word_list=['hello', 'world', 'Python']))


class Command(BaseCommand):

    def handle(self, *args, **options):
        # step_1()
        # step_2()
        # step_3()
        step_4()
