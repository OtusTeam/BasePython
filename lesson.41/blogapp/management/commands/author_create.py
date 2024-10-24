from django.core.management.base import BaseCommand
from blogapp.models import Author


class Command(BaseCommand):
    help = 'Create author'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help="Author name")

    def handle(self, *args, **options):
        name = options.get('name')
        author = Author.objects.create(name=name,
                                       age=40,
                                       email=f'{name}@mail.ru',
                                       bio=f'bio {name}')
        author.save()
        self.stdout.write(self.style.SUCCESS(f'Автор создан: {author}'))