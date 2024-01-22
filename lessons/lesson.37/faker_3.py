import random

import faker
from faker import providers

faker_inst = faker.Faker()


class FoodProvider(providers.BaseProvider):
    def drink(self):
        return random.choice(['water', 'milk', 'juce'])


faker_inst.add_provider(FoodProvider)

print(faker_inst.drink())
print(faker_inst.drink())
