from django.core.management.base import BaseCommand, CommandError
from mainapp.models import Category, Animal, Food
from userapp.models import MyUser

class Command(BaseCommand):
    help = 'Fill db'

    def handle(self, *args, **options):
        # create, update, delete
        # delete
        Food.objects.all().delete()
        Category.objects.all().delete()

        # create superuser
        try:
            MyUser.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        except:
            print('Админ уже был создан раньше')
        # create
        category = Category.objects.create(name='Медведь')
        print(category)
        print(type(category))
        print(category.name)

        # update
        category.name = 'Жук'
        category.save()

        # delete
        category.delete()

        bear = Category.objects.create(name='Медведь')
        parrot = Category.objects.create(name='Попугай')

        # FK
        boris = Animal.objects.create(name='Борис', category=bear)
        leo = Animal.objects.create(name='Лео', category=bear)
        kate = Animal.objects.create(name='Kate', category=parrot)

        # Many to Many
        banana = Food.objects.create(name='Банан')
        seeds = Food.objects.create(name='Семена')
        honey = Food.objects.create(name='Мед')

        # Посмотреть запрос в shell
        bear.foods.clear()
        bear.foods.add(banana)
        bear.foods.add(honey)
        bear.save()

        parrot.foods.clear()
        parrot.foods.add(seeds)
        parrot.foods.add(banana)
        parrot.save()

        # select запросы
        # 1. Выбрать все данные
        print(Category.objects.all())

        # 2. Выбор 1-го
        # 1-ый
        print(Category.objects.all().first())
        # get
        print(Category.objects.get(id=bear.id))
        print(Category.objects.get(id=bear.id).id)

        # 3. Filter
        bears = Category.objects.filter(name='Медведь')
        print(bears)

        bears = Category.objects.filter(name='Медведь', is_active=True)
        print(bears)

        # Взять все катигории с названием не Медведь
        bears = Category.objects.exclude(name='Медведь')
        print(bears)

        # Взять все активные категории, кроме медведь
        bears = Category.objects.filter(is_active=True).exclude(name='Медведь')
        print(bears)

        # Взять категории которые живут больше 30 лет
        categorys = Category.objects.filter(max_age__gt=30)
        print(categorys)
        # Имя категории содержит "ведь"
        categorys = Category.objects.filter(name__contains='ведь')
        print(categorys)

        # выбрать животных с именем категории медведь
        animals = Animal.objects.filter(category__name='Медведь')
        print(animals)
        # выбрать животных с имененм категории на букву М
        animals = Animal.objects.filter(category__name__istartswith='М')
        print(animals)

        print('Many to many')

        # Кто ест банан? M * M
        category = Category.objects.filter(foods=banana)
        print(category)

        # Кто ест банан или семена? M * M
        category = Category.objects.filter(foods__in=[banana, seeds])
        print(category)

        # Кто ест банан или семена? M * M
        category = Category.objects.filter(foods__name__in=['Банан', 'Семена']).distinct()
        print(category)

        print(category)
        print('DONE')