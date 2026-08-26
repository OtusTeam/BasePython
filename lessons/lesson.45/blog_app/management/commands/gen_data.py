from django.core.management.base import BaseCommand
from blog_app.models import Post, Author, Comment, Tag
import random
from faker import Faker


class Command(BaseCommand):
    help = 'Генерация тестовых данных'

    def handle(self, *args, **kwargs):
        """Выполняет создание тестовых данных."""
        self.stdout.write("Начинаем генерацию")

        faker = Faker()

        # Генерация авторов
        authors = []

        for i in range(random.randint(3, 7)):
            author = Author.objects.create(name=faker.first_name())
            authors.append(author)
        self.stdout.write(f"Завершили создание {len(authors)} авторов")

        # Генерация постов
        posts = []
        comments = []

        for _ in range(random.randint(10, 15)):
            post = Post.objects.create(
                title=faker.sentence(nb_words=random.randint(3, 7)),
                author=random.choice(authors),
                content=faker.text(max_nb_chars=random.randint(500, 700)),
                rating=random.randint(1, 10),

            )
            posts.append(post)

            # Генерация комментариев

            for _ in range(random.randint(5, 10)):
                comment = Comment.objects.create(
                    text=faker.text(max_nb_chars=random.randint(300, 500)),
                    author=random.choice(authors),
                    post=post
                )

                comments.append(comment)

        self.stdout.write(f"Завершили создание {len(posts)} постов")
        self.stdout.write(f"Завершили создание {len(comments)} комментариев")

        self.stdout.write("Завершили генерацию")