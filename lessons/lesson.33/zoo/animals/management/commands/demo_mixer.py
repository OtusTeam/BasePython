from django.core.management.base import BaseCommand
from django.utils import timezone
from django.contrib.auth.models import User
from faker import Faker
from mixer.backend.django import mixer

fake = Faker('ru_RU')


class Command(BaseCommand):
    def handle(self, *args, **options):
        animal = mixer.blend(
            'animals.Animal',
            created_at=timezone.now,
            kind=mixer.SELECT,
        )
        print(animal)
        print(vars(animal))
        print(animal.kind)
        print(vars(animal.kind))

        user = mixer.blend(User, username=mixer.MIX.last_name)
        # user = mixer.blend(User, month=mixer.MIX.birth_date.month)
        print(user)
        print(vars(user))

        users = mixer.cycle(3).blend(
            User,
            username=fake.user_name,
            email=mixer.sequence(lambda c: f"user_00{c}@example.com"),
        )
        print(users)
        for user in users:
            print(user.email)
