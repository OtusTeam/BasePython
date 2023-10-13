from mixer.backend.django import mixer

animal = mixer.blend('main.Animal')
print(animal, type(animal))

