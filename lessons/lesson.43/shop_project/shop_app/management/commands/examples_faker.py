from django.core.management import BaseCommand
from faker import Faker

fake = Faker()
# Faker.seed(1000)
# fake = Faker("ru_RU")


class Command(BaseCommand):
    help = "Faker Examples"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Show Faker Examples"))

        for _ in range(3):
            print(fake.name())

        for _ in range(3):
            print("---")
            print(fake.credit_card_full())
            print(fake.date_time_between())
        # self.stdout.write(self.style.ERROR("Example danger"))
        # self.stdout.write(self.style.WARNING("Example warning"))
        self.stdout.write(self.style.SUCCESS("Done"))
