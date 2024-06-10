import random
from django.core.management.base import BaseCommand
from users.models import MyUser


class Command(BaseCommand):

    def handle(self, *args, **options):
        MyUser.objects.create_user(
            username='user3',
            email='user3@user.com',
            password='user3ien38cj',
            is_staff=True,
        )

        MyUser.objects.create_superuser(
            username='admin2',
            email='admin2@user.com',
            password='user3ien38cjdfdfdf',
            is_staff=True,
        )
