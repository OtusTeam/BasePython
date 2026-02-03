import random
from faker import Faker
from django.core.management.base import BaseCommand
from blog_app.models import Post, Author, Comment



class Command(BaseCommand):
    help = 'Генерация данных'

    def handle(self, *args, **kwargs):
        self.stdout.write('Начинаем генерацию данных...')

        fake = Faker()

        authors = []
        for i in range(random.randint(3, 5)):
            author = Author.objects.create(
                name=fake.name(),
            )
            authors.append(author)
        self.stdout.write(f'Создали {len(authors)} авторов')

        posts = []
        for i in range(random.randint(5, 10)):
            post_title = fake.sentence(nb_words=6)
            post_author = random.choice(authors)
            post_content = fake.text(max_nb_chars=200)

            post = Post.objects.create(
                title=post_title,
                content=post_content,
                author=post_author,
                rating=random.randint(1, 5),
            )
            posts.append(post)
        self.stdout.write(f'Создали {len(posts)} постов')

        comments = []
        for i in range(random.randint(7, 15)):
            comment_text = fake.text(max_nb_chars=100)
            comment_author = random.choice(authors)
            comment_post = random.choice(posts)

            comment = Comment.objects.create(
                text=comment_text,
                post=comment_post,
                author=comment_author,
            )
            comments.append(comment)
        self.stdout.write(f'Создали {len(comments)} комментариев')
        self.stdout.write('Генерация данных завершена')
