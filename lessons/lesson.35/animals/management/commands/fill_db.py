from django.core.management.base import BaseCommand

from animals.models import Animal, Kind, Food, AnimalProfile


class Command(BaseCommand):
    help = "Fill Db"

    def handle(self, *args, **options):
        kinds = Kind.objects.all()

        # удаление данных
        kinds.delete()

        # создание
        bear = Kind.objects.create(name='Медведь')
        tiger = Kind.objects.create(name='Тигр')

        leo = Animal.objects.create(
            name='Leo',
            kind=bear,
            # kind_id=1,
        )

        boris = Animal.objects.create(
            name='Boris',
            kind=bear,
        )

        kate = Animal.objects.create(
            name='Kate',
            kind=tiger,
        )

        meat = Food.objects.create(name='meat')
        meat.animal.add(leo)
        meat.animal.add(kate)

        berry = Food.objects.create(name='berry')
        berry.animal.add(boris)
        berry.animal.add(leo)

        self.stdout.write(
            self.style.SUCCESS('DB is ready')
        )
