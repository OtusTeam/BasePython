from django.core.management.base import BaseCommand
from animals.models import Animal, Category


class Command(BaseCommand):
    help = "Fill Db"

    def handle(self, *args, **options):
        # создание, удаление, обновление данных 3 запроса
        # получение всех данных, получение 1-го объекта

        # получение всех данных
        categories = Category.objects.all()

        # удаление данных
        categories.delete()

        # создание
        bear = Category.objects.create(name='Медведь')
        tiger = Category.objects.create(name='Тигр')
        to_delete = Category.objects.create(name='To delete')

        # удаление
        to_delete.delete()

        print(bear.name)

        # обновление
        bear.name = 'Черепаха'
        bear.save()

        print(bear.name)

        # получение одного объекта
        # получение 1-го объекта
        first_category = Category.objects.all().first()
        print(first_category)
        print(type(first_category))

        # получение конкретного объекта
        turtle = Category.objects.get(name='Черепаха')
        print(turtle)
        print(type(turtle))

        leo = Animal.objects.create(
            name='Leo',
            category=bear,
        )

        boris = Animal.objects.create(
            name='Boris',
            category=bear,
        )

        kate = Animal.objects.create(
            name='Kate',
            category=tiger,
        )

        self.stdout.write(
            self.style.SUCCESS('Hello command')
        )