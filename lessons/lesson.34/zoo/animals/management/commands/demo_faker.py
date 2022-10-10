from django.core.management.base import BaseCommand
from faker import Faker

Faker.seed("sohidufghdghfgddjgfdfhgfb")
fake = Faker("ru_RU")


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write(
            self.style.WARNING("Hello Faker")
        )

        # _name = "Vasya"
        # _na = "Vasya"
        # _n = "Vasya"
        # _ = "Vasya"
        # a-z A-Z 0-9 _

        # for _ in range(0):
        #     ...
        #
        # assert _ == 0

        # self.stdout.write(
        #     str(
        #         fake.pyint(min_value=1, max_value=100)
        #     )
        # )

        self.stdout.write(
            fake.pystr()
        )

        self.stdout.write(
            fake.user_name()
        )

        self.stdout.write(
            str(
                fake.pyint(min_value=1, max_value=100)
            )
        )

        self.stdout.write(
            fake.name()
        )

        self.stdout.write(
            str(
                fake.pyint(min_value=1, max_value=100)
            )
        )

        self.stdout.write(
            fake.name()
        )

        self.stdout.write(
            fake.user_name()
        )

        self.stdout.write(
            fake.name()
        )

        self.stdout.write(
            fake.first_name()
        )

        self.stdout.write(
            fake.first_name()
        )

        self.stdout.write(
            fake.last_name()
        )

        self.stdout.write(
            fake.last_name()
        )

        self.stdout.write(
            fake.name()
        )

        self.stdout.write(
            self.style.WARNING("emails:")
        )
        self.stdout.write(
            fake.ascii_company_email()
        )

        self.stdout.write(
            fake.ascii_company_email()
        )

        self.stdout.write(
            fake.email()
        )

        self.stdout.write(
            fake.email()
        )

        self.stdout.write(
            self.style.WARNING("jobs:")
        )

        self.stdout.write(
            fake.job()
        )
        self.stdout.write(
            fake.job()
        )

        self.stdout.write(
            self.style.SUCCESS("Bye Faker!")
        )
