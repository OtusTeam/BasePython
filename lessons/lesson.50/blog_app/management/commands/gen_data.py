import random
from django.core.management.base import BaseCommand
from blog_app.models import Post, Author, Comment



class Command(BaseCommand):
    help = 'Генерация данных'

    def handle(self, *args, **kwargs):
        self.stdout.write('Начинаем генерацию данных...')

        authors = []
        for i in range(5):
            author = Author.objects.create(name=f'Author {i + 1}')
            authors.append(author)
        self.stdout.write(f'Создали {len(authors)} авторов')

        posts = []
        for i in range(5):
            post_title = f'Post {i + 1}'
            post_author = random.choice(authors)
            post_content = f'Контент {i + 1}'

            post = Post.objects.create(
                title=post_title,
                content=post_content,
                author=post_author,
                rating=random.randint(1, 5),
            )
            posts.append(post)
        self.stdout.write(f'Создали {len(posts)} постов')

        comments = []
        for i in range(5):
            comment_text = f'Комментарий {i + 1}'
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
