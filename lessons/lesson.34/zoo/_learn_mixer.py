import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zoo.settings')
import django

django.setup()

from animals.models import Animal

print(vars(Animal))
