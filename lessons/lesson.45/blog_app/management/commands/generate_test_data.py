from django.core.management.base import BaseCommand
from blog_app.models import Post, Comment, Tag, Author, AuthorProfile
from faker import Faker


class Command(BaseCommand):
    help = 'Generate test data'

    def handle(self, *args, **kwargs):
        self.stdout.write("Generating test data...")

        # authors = []
        faker = Faker()
        for _ in range(5):
            author = Author.objects.create(
                name=faker.name())
            # authors.append(author)
            self.stdout.write("Author created")

            for _ in range(10):
                post_title = faker.sentence()
                post_content = faker.text()
                post_author = author
                post_rating = faker.random_int(min=1, max=10)

                post = Post.objects.create(
                    title=post_title,
                    content=post_content,
                    author=post_author,
                    rating=post_rating,
                )

                for _ in range(5):
                    comment_text = faker.sentence()
                    comment_author = author
                    comment_post = post

                    Comment.objects.create(
                        text=comment_text,
                        author=comment_author,
                        post=comment_post,
                    )

        self.stdout.write("Test data generated DONE")