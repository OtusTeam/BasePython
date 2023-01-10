from factory.django import DjangoModelFactory
import factory
from .models import Category, Animal


class CategoryFactory(DjangoModelFactory):
    class Meta:
        # model = 'myapp.User'  # Equivalent to ``model = myapp.models.User``
        model = Category  # Equivalent to ``model = myapp.models.User``

    name = 'Parrot'


class AnimalFactory(DjangoModelFactory):
    class Meta:
        model = Animal

    name = factory.Faker('name')
    # color = factory.Faker('color')
    category = factory.SubFactory(CategoryFactory)