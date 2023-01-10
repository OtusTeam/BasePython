from django.core.management.base import BaseCommand, CommandError
from animals.models import Animal, Category, Card, Food


class Command(BaseCommand):
    help = 'Fill db'

    def handle(self, *args, **options):
        # create, update, delete, выборка всех объектов, выборка 1 объекта
        # filter
        # 1. DELETE
        print('Start')
        print('Удаляем старые данные')
        Card.objects.all().delete()
        Animal.objects.all().delete()
        Category.objects.all().delete()
        Food.objects.all().delete()

        # 2. Создание
        print('Создаю новые данные')
        bear_category = Category.objects.create(name='Медведь')
        print(bear_category.name)
        # 3. Обновление
        print('Обновляю')
        bear_category.name = 'Попугай'
        bear_category.save()
        print(bear_category.name)

        parrot = Animal.objects.create(name='Карл', category=bear_category)

        print(parrot)
        parrot_id = parrot.id
        print('ID', parrot_id)

        card = Card.objects.create(text='Карл приехали к нам с кубы', animal=parrot)
        print(card)

        print('создаю еду')
        proso = Food.objects.create(name='Пшеница')
        proso.animals.add(parrot)
        proso.save()

        tiger_category = Category.objects.create(name='Тигр')
        tiger = Animal.objects.create(name='Кабзон', category=tiger_category)

        banana = Food.objects.create(name='Банан')
        banana.animals.add(parrot)
        banana.animals.add(tiger)
        banana.save()

        foods = Food.objects.all()
        print(type(foods))

        print('---------ALL FOOD------------')
        for food in foods:
            print('------->food')
            print(food.name)
            for animal in food.animals.all():
                print('animal--------!')
                print(animal.name)
                print(animal.category.name)

        # Найти по ID
        # Когда всегда есть элемент
        one_element = Animal.objects.get(id=parrot_id)
        print(one_element)

        # Первый элемент
        one_element = Animal.objects.filter(id=parrot_id).first()
        print(one_element)

        # Фильтры
        # 1. Найти животное по имени
        animals = Animal.objects.filter(name='Карл')
        print(animals)
        # 2. Найти животное по имени и возрасту
        animals = Animal.objects.filter(name='Карл', age=0)
        print(animals)
        # 3. Найти животное по части имени
        animals = Animal.objects.filter(name__contains='Ка')
        print(animals)
        animals = Animal.objects.filter(name__icontains='ка')
        print(animals)
        animals = Animal.objects.filter(name__contains='ка')
        print(animals)
        animals = Animal.objects.filter(name__startswith='Ка')
        print(animals)
        # 4. Найти животное по части имени и границе возраста меньшей
        animals = Animal.objects.filter(name__contains='ар', age__gte=0, age__lt=10)
        print(animals)
        # 5. Найти животное по имени категории
        animals = Animal.objects.filter(category__name='Тигр')
        print(animals)
        # 6. Найти животное по совпадению имени категории
        animals = Animal.objects.filter(category__name__contains='иг')
        print(animals)
        # TODO: Найти категории всех животных, которые едят еду с именем Банан - distinct
        # 7. Найти категории всех животных, которые едят еду с именем Банан - distinct

        print('Categories banana')
        foods = Food.objects.filter(name='Банан')
        for food in foods:
            for animal in food.animals.all():
                print(animal.category)

        print('End')