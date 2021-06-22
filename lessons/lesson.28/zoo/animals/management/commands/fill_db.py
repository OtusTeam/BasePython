from django.core.management.base import BaseCommand
from animals.models import Family, Kind, Food, Animal


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Удаление objects - менеджер модели
        Family.objects.all().delete()
        # Создание
        bear = Family.objects.create(name='Медведь')
        print(bear.id)
        kind = Kind.objects.create(name='Бурый', family=bear)
        kind2 = Kind.objects.create(name='Черный', family=bear)
        print(kind.id)

        # ManyToMany
        food = Food.objects.create(name='Мёд')
        food.kinds.add(kind)
        food.kinds.add(kind2)

        print(food.kinds.all())

        # Изменение
        bear.name = 'Тигр'
        bear.save()
        print(bear.name)
        kind.name = 'Белый'
        kind.save()
        print(kind.name)

        print('end')

        # 3 Основных запроса
        # 1. Получить всё
        families = Family.objects.all()
        print(type(families))
        print(families)
        for family in families:
            print(type(family))
            print(family.name)

        # 2. Получить несколько объектов по условию (фильтр)
        # Получить виды с именем Черный
        blacks = Kind.objects.filter(name='Черный')
        # blacks = Kind.objects.filter(<условия на поля>)
        print(type(blacks))
        print(blacks)
        for item in blacks:
            print(item.name)

        # 3. Получить один объект
        # - первый
        # Получить 1-го черного медведя
        first_black = Kind.objects.filter(name='Черный').first()
        print('---------------')
        print(type(first_black))
        print(first_black.name)
        first_black = Kind.objects.filter(name='Что то пошло не так').first()
        print('---------------')
        print(first_black)

        # - только один объект (обычно берем по id)
        first_black = Kind.objects.get(name='Черный')
        print('---------------')
        print(type(first_black))
        print(first_black.name)
        # first_black = Kind.objects.get(name='Что то пошло не так')
        # print('---------------')
        # print(first_black)

        # Более сложные фильтры
        # Фильтр связанной модели
        animal = Animal.objects.create(name='Борис', kind=kind)
        print(animal.id)

        # Найти животных имя вида которых Белый
        animals = Animal.objects.filter(kind__name='Черный')
        print(animals)
        # Найти животных имя семейства которых Тигр
        animals = Animal.objects.filter(kind__family__name='Тигр')
        print(animals)

        print('RESULT')
        # Найти животных имя семейсвто которых начинается с буквы Т
        animals = Animal.objects.filter(kind__family__name__startswith='Т')
        print(animals)
        print(animals.first().name)
        print(animals[0].name)
        print(animals.first())
        print(animals.first().kind.family.name)
        # Найти животных имя вида которых содержит "елы"
        animals = Animal.objects.filter(kind__name__contains='елы')
        print(animals)

