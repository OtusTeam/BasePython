import random
from django.core.management.base import BaseCommand
from animals.models import Category, Animal, Food


class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Get animals ...')
        print('Получить все категории')
        print(Category.objects.all())
        # Filters
        print('Получить все категории с названием Медведь')
        print(Category.objects.filter(name='Медведь'))
        print('Получить все категории у которые название не Медведь')
        print(Category.objects.exclude(name='Медведь'))
        print('Получить все категории с именем Медведь и у которых имя не Тигр')
        print(Category.objects.filter(name='Медведь').exclude(name='Тигр'))
        print('Получить всех животных с возрастом 100 лет')
        print(Animal.objects.filter(age=100))
        print('Получить количество животных с возрастом больше 100 лет')
        print(Animal.objects.filter(age__gt=100).count())
        print('Получить количество животных с возрастом меньше равно 100 лет')
        print(Animal.objects.filter(age__lte=100).count())
        print('Больше 10 лет и меньше 37 лет')
        print(Animal.objects.filter(age__gt=10, age__lt=37).count())
        print('Получить категорию название которой начаниется на Че')
        print(Category.objects.filter(name__startswith='Че'))
        print('Получить категорию название которой содержит на ве')
        print(Category.objects.filter(name__contains='ве'))
        print('Получить все медведей')
        bear = Category.objects.get(name='Медведь')
        print(Animal.objects.filter(category=bear))
        print(Animal.objects.filter(category__name='Медведь'))

        print('Получить всех животных у которых имя категории начинается на Че')

        print(Animal.objects.filter(category__name__startswith='Че'))

