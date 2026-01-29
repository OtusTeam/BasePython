from faker import Faker
from django.core.management.base import BaseCommand
from blog_app.models import Post, Comment, Author, Tag, AuthorProfile
import random


class Command(BaseCommand):
    help = 'Генерация тестовых данных'

    def handle(self, *args, **kwargs):
        self.stdout.write('Начинаем генерацию данных')

        fake = Faker()

        authors = []
        for i in range(random.randint(3, 7)):
            author = Author.objects.create(name=fake.name())
            authors.append(author)
        self.stdout.write('Завершили создание авторов')

        posts = []
        for i in range(random.randint(5, 10)):
            post = Post.objects.create(
                title=fake.sentence(nb_words=5),
                author=random.choice(authors),
                content=fake.text(max_nb_chars=300),
                rating=random.randint(1, 10),
            )
            posts.append(post)
        self.stdout.write('Завершили создание посты')

        for i in range(1, 6):
            Comment.objects.create(
                text=fake.text(max_nb_chars=100),
                author=random.choice(authors),
                post=random.choice(posts),
            )
        self.stdout.write('Завершили создание комментов')

        self.stdout.write('Завершили генерацию данных')