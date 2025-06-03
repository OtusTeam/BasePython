import factory
from faker import Faker
from blog_app.models import Author


fake = Faker()


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author

    name = factory.Faker('name')
