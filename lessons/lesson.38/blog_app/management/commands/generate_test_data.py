from blog_app.models import Author, Post, Comment
from django.core.management.base import BaseCommand
from faker import Faker
import random


class Command(BaseCommand):
    help = 'Генерация тестовых данных'

    def handle(self, *args, **kwargs):
        self.stdout.write("Начинаем генерацию авторов...")

        fake = Faker()

        authors = []
        for _ in range(5):
            author_name = fake.name
            author = Author.objects.create(name=author_name)
            authors.append(author)
        self.stdout.write("Создали 10 авторов")

        self.stdout.write("Начинаем генерацию постов...")

        for _ in range(20):
            post_title = fake.sentence(nb_words=6)
            post_content = fake.text(max_nb_chars=200)
            post_author = random.choice(authors)
            post = Post.objects.create(
                title = post_title,
                content = post_content,
                author = post_author,
                rating = random.randint(1, 10)
            )
        self.stdout.write("Создали 20 постов")


