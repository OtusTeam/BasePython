import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.settings")

import django

django.setup()

from mixer.backend.django import mixer

animal = mixer.blend('animals.Animal')
print(animal)
