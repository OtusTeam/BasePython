from django.core.management.base import BaseCommand
from faker import Faker
from blog_app.models import Post, Author

# import random


class Command(BaseCommand):
    help = 'Generate test data'

    def handle(self, *args, **kwargs):

        self.stdout.write('Start generating test data')
        faker = Faker()
        for _ in range(10):
            author = Author.objects.create(
            name=f'{faker.first_name()} {faker.last_name()}'
            )
            for _ in range(7):
                Post.objects.create(
                    title=faker.sentence(),
                    content=faker.text(),
                    author=author
                )
            self.stdout.write('Автор создан')

        self.stdout.write('Stop generating test data')
