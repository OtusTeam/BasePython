from django.core.management.base import BaseCommand

from animals.models import Animal, AnimalDetail


class Command(BaseCommand):

    def handle(self, *args, **options):
        # to_update_animals = Animal.objects.filter(kind__id=1)
        # kind = AnimalKind.objects.filter(name='lion').first()
        # try:
        #     kind = AnimalKind.objects.get(name='bird')
        # except Exception as e:
        #     print(e)
        # print(kind, type(kind))

        # to_update_animals = Animal.objects.filter(kind__id=1)
        # to_update_animals = Animal.objects.filter(kind=kind)
        # to_update_animals = Animal.objects.filter(kind__name='lion')
        # to_update_animals = Animal.objects.filter(kind__name__in=('lion', 'monkey'))
        # to_update_animals = Animal.objects.filter(age=3)
        # to_update_animals = Animal.objects.filter(age__gt=3)
        # to_update_animals = Animal.objects.filter(age__gte=3)
        to_update_animals = Animal.objects.filter(animaldetail__isnull=True)
        # print(to_update_animals.query)
        # print(to_update_animals)
        for animal in to_update_animals:
            AnimalDetail.objects.create(
                animal=animal,
                biography='to be filled'
            )
            print(f'for {animal} detail created')
