import random

import faker
import faker_music
from faker import providers

faker.Faker.seed("zoo-tests")


class FoodProvider(providers.BaseProvider):
    def drink(self):
        return random.choice(['water', 'milk', 'juce'])


faker_inst = faker.Faker('ru_RU')
# faker_inst = faker.Faker('es_ES')
# faker_inst = faker.Faker()

# print(faker_inst.name(), type(faker_inst.name()))
# print(faker_inst.address(), type(faker_inst.address()))


faker_inst.add_provider(faker_music.MusicProvider)
faker_inst.add_provider(FoodProvider)

print(faker_inst.music_genre())
print(faker_inst.drink())
