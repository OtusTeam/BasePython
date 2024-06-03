import random
from django.core.management.base import BaseCommand
from animals.models import Category, Animal, Food


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

        tiger = Category.objects.create(
            name='Тигр',
        )

        turtle = Category(
            name='Черепаха'
        )

        turtle.save()

        category_list = [
            bear,
            tiger,
            turtle,
        ]

        # 4. Все данные
        print(Category.objects.all())

        Animal.objects.all().delete()

        # 5. получить только 1 объект
        # bear = Category.objects.get(id=bear.id)

        ANIMAL_COUNT = 300

        animals_to_create = []
        for i in range(ANIMAL_COUNT):
            random_category = random.choice(category_list)

            animal = Animal(
                name=f'animal_{i}',
                # category='Медведь'? bear ? bear.id
                category=random_category,
                age=random.randint(1,200)
            )
            animals_to_create.append(animal)

        Animal.objects.bulk_create(animals_to_create)

        print(Animal.objects.all().count())
        print('Done')

        food_names = [
            'Банан',
            'Яблоко',
            'Мясо',
            'Мёд',
            'Рыба',
        ]

        Food.objects.all().delete()

        for name in food_names:
            Food.objects.create(name=name)

        print(Food.objects.all().count())

        all_animals = Animal.objects.all()

        for animal in all_animals:
            food_count = random.randint(1,5)
            random_food_names = random.sample(food_names, food_count)

            for name in random_food_names:
                random_food = Food.objects.get(name=name)
                # Many to many save
                animal.food.add(random_food)
            animal.save()
