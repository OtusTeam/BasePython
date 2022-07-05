from django.core.management.base import BaseCommand

from animals.models import AnimalFood


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write("Create some foods")

        foods = []
        food_names = ["milk", "banana", "sausages"]
        for name in food_names:
            food, created = AnimalFood.objects.get_or_create(name=name)
            foods.append(food)

        self.stdout.write(f"Created foods: {foods}")
