
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils import timezone
from mixer.backend.django import mixer

from animals.models import AnimalKind


class Command(BaseCommand):
    def handle(self, *args, **options):
        animal_kind = mixer.blend(AnimalKind)
        print(animal_kind, animal_kind.pk)

        # animal = mixer.blend('animals.animal')
        animal = mixer.blend(
            "animals.animal",
            # kind=animal_kind,
            # created_at=timezone.now,
            # created_at=mixer.FAKE,
            kind=mixer.SELECT,
        )
        print(animal, animal.pk, animal.kind, animal.kind.pk)

        user: User = mixer.blend(
            User,
            last_name=mixer.MIX.username,
        )
        print(user, user.username, user.last_name, user.first_name)

        users: list[User] = mixer.cycle(3).blend(
            User,
            # username=mixer.FAKE,
            # last_name=fake.last_name,
            email=mixer.sequence(
                lambda c: f"user_{c}@example.com"
            )
        )
        for user in users:
            print(user.email)

