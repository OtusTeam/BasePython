from django.core.management.base import BaseCommand
from blog_app.models import Post, Author, Comment, Tag
from faker import Faker
import random


class Command(BaseCommand):
    help = 'Генерация тестовых данных Post, Author, Comment, Tag'

    def handle(self, *args, **kwargs):
        self.stdout.write("Начинается генерация данных")

        fake = Faker()

        authors = []
        for _ in range(5):
            author_name = fake.name()
            author = Author.objects.create(name=author_name)
            authors.append(author)

        posts = []
        for _ in range(10):
            post_title = fake.sentence(nb_words=5)
            post_content = fake.text(max_nb_chars=200)
            post_author = random.choice(authors)
            post = Post.objects.create(
                title=post_title,
                content=post_content,
                author=post_author,
                rating=random.randint(1, 10)
            )
            posts.append(post)

        comments = []
        for _ in range(20):
            comment_text = fake.text(max_nb_chars=100)
            comment_author = random.choice(authors)
            comment_post = random.choice(posts)
            comment = Comment.objects.create(
                text=comment_text,
                post=comment_post,
                author=comment_author,
            )
            comments.append(comment)

        self.stdout.write(f"Создано {len(comments)} комментариев")
