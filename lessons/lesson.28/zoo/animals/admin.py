from django.contrib import admin

# Register your models here.
from animals.models import Animal

admin.site.register(Animal)
