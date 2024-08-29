from django.core.management.base import BaseCommand

from shop_app.models import Category
from my_auth.models import ShopUser


class Command(BaseCommand):
    help = "Fill Db"

    def handle(self, *args, **options):
        categories = Category.objects.all()

        # удаление данных
        categories.delete()

        # создание
        laptop = Category.objects.create(name='laptop')
        phone = Category.objects.create(name='phone')
        pc = Category.objects.create(name='pc')

        su = ShopUser.objects.filter(username='otus').first()
        if not su:
            ShopUser.objects.create_superuser(
                username='otus',
                email='admin@otus.local',
                password='pass',
            )

        self.stdout.write(
            self.style.SUCCESS('DB is ready')
        )
