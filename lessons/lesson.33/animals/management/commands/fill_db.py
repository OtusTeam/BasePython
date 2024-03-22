from django.core.management.base import BaseCommand

from animals.models import Animal


class Command(BaseCommand):
    help = "Fill Db"

    def handle(self, *args, **options):
        leo = Animal.objects.create(
            name='Leo',
            kind='bear',
        )

        boris = Animal.objects.create(
            name='Boris',
            kind='bear',
        )

        kate = Animal.objects.create(
            name='Kate',
            kind='tiger',
        )

        self.stdout.write(
            self.style.SUCCESS('Hello command')
        )
