from django.core.management.base import BaseCommand
from blog_app.models import Post, Author, AuthorProfile, Comment, Tag
import random
from faker import Faker


class Command(BaseCommand):
    help = 'Генерация тестовых данных'

    def handle(self, *args, **kwargs):
        """Выполняет создание тестовых данных."""
        self.stdout.write("Начинаем генерацию.")

        fake = Faker()

        # Генерация авторов
        authors = []
        for i in range(random.randint(3, 7)):
            author = Author.objects.create(name=fake.first_name())
            authors.append(author)
        self.stdout.write(f"Завершили создание {len(authors)} авторов.")

        # Генерация постов
        posts = []
        comments = []
        for i in range(random.randint(10, 15)):
            post = Post.objects.create(
                title=fake.sentence(nb_words=random.randint(3, 7)),
                author=random.choice(authors),
                content=fake.text(max_nb_chars=500),
                rating=random.randint(1, 10),
            )
            posts.append(post)

            # Генерация комментариев

            for i in range(random.randint(2, 7)):
                comment = Comment.objects.create(
                    text=fake.text(max_nb_chars=500),
                    author=random.choice(authors),
                    post=post
                )
                comments.append(comment)
        self.stdout.write(f"Завершили создание {len(comments)} комментариев.")

        self.stdout.write(f"Завершили создание {len(posts)} постов.")

        self.stdout.write("Закончили генерацию.")