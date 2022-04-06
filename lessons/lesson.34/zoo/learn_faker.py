import random

from faker import Faker
from faker.providers import BaseProvider
from faker_music import MusicProvider

faker = Faker('ru_RU')
faker.add_provider(MusicProvider)
print(faker.name())
print(faker.email())
print(faker.address())
print(faker.music_genre())


class FoodProvider(BaseProvider):
    def drink(self):
        return random.choice(['water', 'milk', 'juce'])


faker.add_provider(FoodProvider)
print(faker.drink())
