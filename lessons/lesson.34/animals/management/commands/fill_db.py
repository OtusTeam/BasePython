from django.core.management.base import BaseCommand
from animals.models import Category, Animal


class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Fill db ...')
        # 1. Удаление
        Category.objects.all().delete()

        # 2. Создание
        bear = Category.objects.create(
            name='Медведь Неправильный',
        )

        # 3. Изменение
        bear.name = 'Медведь'
        bear.save()

        # 4. Все данные
        print(Category.objects.all())

        Animal.objects.all().delete()

        # 5. получить только 1 объект
        # bear = Category.objects.get(id=bear.id)
        bear = Category.objects.get(name='Медведь')

        Animal.objects.create(
            name='Маша',
            # category='Медведь'? bear ? bear.id
            category=bear,
        )

        print('Done')
