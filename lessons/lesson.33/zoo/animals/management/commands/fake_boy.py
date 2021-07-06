from django.core.management.base import BaseCommand
from animals.models import Family, Kind, Animal
import factory


class Command(BaseCommand):

    def handle(self, *args, **options):
        class FamilyFactory(factory.django.DjangoModelFactory):
            class Meta:
                # model = 'animals.Family'
                model = Family

            # name = 'Медведь'
            name = factory.Faker('name')
            # color = factory.Faker('color')

        # далить всё
        Family.objects.all().delete()

        # сохраняет в базу
        family = FamilyFactory.create()
        print('name', family.name)
        print(family.id)

        # не сохранять в базу
        family = FamilyFactory.build(name='Тигр')
        print('name', family.name)
        print(family.id)
        print(family.get_some_error(0))

        class KindFactory(factory.django.DjangoModelFactory):
            class Meta:
                model = Kind

            name = factory.Faker('name')
            family = factory.SubFactory(FamilyFactory)

        kind = KindFactory.create()
        print(kind.family.name)

        # Другие варианты
        # 1. Несколько значений
        # Не сохранять в базу
        families = FamilyFactory.build_batch(3)
        print(families)
        families = FamilyFactory.create_batch(3)
        print(families)

        # 3. Итератор
        families = FamilyFactory.build_batch(5, name=factory.Iterator(['Тигр', 'Черепаха', 'Медведь']))
        for family in families:
            print(family.id)
            print(family.name)

        print('*' * 10)

        # 4. Последовательность
        families = FamilyFactory.build_batch(3, name=factory.Sequence(lambda n: f'number{n}'))
        for family in families:
            print(family.id)
            print(family.name)

        # далить всё
        Family.objects.all().delete()
