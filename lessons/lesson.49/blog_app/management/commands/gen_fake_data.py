import random
from faker import Faker
from django.core.management.base import BaseCommand
from blog_app.models import Post, Author, Comment



class Command(BaseCommand):
    help = "Генерация фейковых данных"

    def handle(self, *args, **kwargs):
        self.stdout.write("Начинаем генерацию....")

        fake = Faker()

        authors = []
        for i in range(5):
            author_name = fake.first_name()
            author = Author.objects.create(name=author_name)
            authors.append(author)
        self.stdout.write(f"Создали {len(authors)} авторов")

        posts = []
        for i in range(10):
            post_title = fake.sentence(nb_words=5)
            post_content = fake.text(max_nb_chars=300)
            post_author = random.choice(authors)
            post = Post.objects.create(
                title=post_title,
                content=post_content,
                author=post_author,
                rating=random.randint(1, 5),
            )
            posts.append(post)
        self.stdout.write(f"Создали {len(posts)} постов")

        comments = []
        for i in range(20):
            comment_text = fake.text(max_nb_chars=100)
            comment_post = random.choice(posts)
            comment_author = random.choice(authors)
            comment = Comment.objects.create(
                text=comment_text,
                post=comment_post,
                author=comment_author,
            )
            comments.append(comment)
        self.stdout.write(f"Создали {len(comments)} комментариев")

        self.stdout.write("Завершили генерацию!")
