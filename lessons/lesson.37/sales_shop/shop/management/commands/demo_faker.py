from django.core.management import BaseCommand

from faker import Faker
from faker_music import MusicProvider

# fake = Faker(locale="de_DE")
fake = Faker(locale="ru_RU")
fake.add_provider(MusicProvider)


Faker.seed("fake-seed-for-demo-faker")


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Start faker")

        self.stdout.write(
            str(
                fake.pyint()
            )
        )
        self.stdout.write(
            fake.pystr()
        )
        self.stdout.write(
            fake.pystr()
        )

        print()

        self.stdout.write(
            fake.name()
        )
        self.stdout.write(
            fake.name()
        )

        self.stdout.write(
            fake.user_name()
        )
        self.stdout.write(
            fake.user_name()
        )
        self.stdout.write(
            fake.user_name()
        )
        self.stdout.write(
            fake.password()
        )

        self.stdout.write(
            fake.phone_number()
        )
        self.stdout.write(
            fake.phone_number()
        )
        self.stdout.write(
            fake.phone_number()
        )
        self.stdout.write(
            fake.ascii_company_email()
        )
        self.stdout.write(
            fake.ascii_company_email()
        )
        self.stdout.write(
            fake.ascii_company_email()
        )

        print()
        self.stdout.write(
            fake.music_genre()
        )
        self.stdout.write(
            fake.music_genre()
        )
        self.stdout.write(
            fake.music_genre()
        )

        self.stdout.write(
            fake.music_instrument()
        )
        self.stdout.write(
            fake.music_instrument()
        )
        self.stdout.write(
            fake.music_instrument()
        )
