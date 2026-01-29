from django.core.management.base import BaseCommand
from blog_app.models import Post, Comment, Author, Tag, AuthorProfile
import random


class Command(BaseCommand):
    help = 'Генерация тестовых данных'

    def handle(self, *args, **kwargs):
        self.stdout.write('Начинаем генерацию данных')

        authors = []
        for i in range(1, 6):
            author = Author.objects.create(name=f'Author {i}')
            authors.append(author)
        self.stdout.write('Завершили создание авторов')

        posts = []
        for i in range(1, 6):
            post = Post.objects.create(
                title=f'Post {i}',
                author=random.choice(authors),
                content=f'Content {i}',
                rating=random.randint(1, 10),
            )
            posts.append(post)
        self.stdout.write('Завершили создание посты')

        for i in range(1, 6):
            Comment.objects.create(
                text=f'Comment {i}',
                author=random.choice(authors),
                post=random.choice(posts),
            )
        self.stdout.write('Завершили создание комментов')

        self.stdout.write('Завершили генерацию данных')