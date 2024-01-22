import faker
import faker_music

faker_inst = faker.Faker()

faker_inst.add_provider(faker_music.MusicProvider)

print(faker_inst.music_genre_object())
print(faker_inst.music_instrument())
