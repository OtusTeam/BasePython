from django.core.management.base import BaseCommand

from animals.models import Animal, Kind, Food, AnimalProfile


class Command(BaseCommand):
    help = "Fill Db"

    def handle(self, *args, **options):
        pass
        # animal = Animal.objects.get(id=5)  # -> exc
        # animal = Animal.objects.filter(id=5).first()  # -> None



