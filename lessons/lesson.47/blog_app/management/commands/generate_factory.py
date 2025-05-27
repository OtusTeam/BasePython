from django.core.management.base import BaseCommand
from blog_app.factories import AuthorFactory
# import random


class Command(BaseCommand):
    help = 'Generate test data'

    def handle(self, *args, **kwargs):

        self.stdout.write('Start generating Author')

        authors = AuthorFactory.create_batch(10)

        self.stdout.write('Stop generating Author')
