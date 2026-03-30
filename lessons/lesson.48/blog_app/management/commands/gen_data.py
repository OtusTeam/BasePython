import random
from faker import Faker
from django.core.management.base import BaseCommand
from blog_app.models import Author, Comment, Post


class Command(BaseCommand):
    help = "Генерация тестовых данных"

    def handle(self, *args, **kwargs):
        self.stdout.write("Начинаем генерацию данных")

        fake = Faker()

        authors = []
        for _ in range(random.randint(3, 7)):
            author = Author.objects.create(name=fake.first_name())
            authors.append(author)
        self.stdout.write(f"Завершили создание {len(authors)} авторов")

        posts = []
        for _ in range(random.randint(5, 10)):
            post = Post.objects.create(
                title=fake.sentence(nb_words=random.randint(2, 5)),
                author=random.choice(authors),
                content=fake.text(max_nb_chars=300),
                rating=random.randint(1, 10),
            )
            posts.append(post)
        self.stdout.write(f"Завершили создание {len(posts)} постов")

        comments = []
        for _ in range(1, 5):
            comment = Comment.objects.create(
                text=fake.text(max_nb_chars=100),
                author=random.choice(authors),
                post=random.choice(posts),
            )
            comments.append(comment)
        self.stdout.write(f"Завершили создание {len(comments)} коментов")

        self.stdout.write("Закончили генерацию данных")
