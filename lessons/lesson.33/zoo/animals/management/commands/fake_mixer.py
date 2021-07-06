from django.core.management.base import BaseCommand
from mixer.backend.django import mixer
from animals.models import Family, Kind, Animal


class Command(BaseCommand):

    def handle(self, *args, **options):
        # далить всё
        Family.objects.all().delete()

        family = mixer.blend(Family)
        print(family.name)

        kind = mixer.blend(Kind)
        print(kind.name)
        print(kind.family.name)

        animal = mixer.blend(Animal)
        print(animal.kind.family.name)

        # Частичное задание данных
        kind = mixer.blend(Kind, name='Бурый')
        print(kind.name, kind.family.name)

        # 1. способ
        family = mixer.blend(Family, name='Медведь')
        kind = mixer.blend(Kind, family=family)
        print(kind.name, kind.family.name)

        # 2. способ
        kind = mixer.blend(Kind, family__name='Тигр')
        print(kind.name, kind.family.name)

        animal = mixer.blend(Animal, kind__family__name='Черепаха')

        # далить всё
        Family.objects.all().delete()

        family = mixer.blend(Family, name=mixer.RANDOM('Тигр', 'Черепаха', 'Медведь'))
        print(family.name)

        # далить всё
        Family.objects.all().delete()
        # замешать несколько значений
        # 1. случайных
        families = mixer.cycle(3).blend(Family)
        print(families)

        # далить всё
        Family.objects.all().delete()
        # 2. последовательность

        families = mixer.cycle(4).blend(Family, name=mixer.sequence('Тигр', 'Черепаха', 'Медведь'))
        for family in families:
            print(family.name)

        # далить всё
        Family.objects.all().delete()