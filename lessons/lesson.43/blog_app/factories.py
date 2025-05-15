import factory
from blog_app.models import Comment, Post, Tag, Author
from faker import Faker
import random


fake = Faker()


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author

    name = factory.Faker('name')
