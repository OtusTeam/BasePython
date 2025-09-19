import random
from django.core.management.base import BaseCommand
from blog_app.models import Post, Author, Comment



class Command(BaseCommand):
    help = "Генерация тестовых данных"

    def handle(self, *args, **kwargs):
        self.stdout.write("Начинаем генерацию....")

        authors = []
        for i in range(5):
            author_name = f"Автор {i + 1}"
            author = Author.objects.create(name=author_name)
            authors.append(author)
        self.stdout.write(f"Создали {len(authors)} авторов")

        posts = []
        for i in range(10):
            post_title = f"Пост {i + 1}"
            post_content = f"Это контент {i + 1}"
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
            comment_text = f"Комментарий {i + 1}"
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
