import faker
from faker.providers import BaseProvider
import faker_music

f_instance = faker.Faker('ru_ru')
# f_instance = faker.Faker()


class FoodProvider(BaseProvider):
    def food(self):
        return 'meat'


f_instance.add_provider(FoodProvider)
f_instance.add_provider(faker_music.MusicProvider)

print(f_instance.sentence())
print(f_instance.food())
print(f_instance.music_genre())
print(f_instance.address())
