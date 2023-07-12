__all__ = ("fake",)

from faker import Faker

Faker.seed("django-sales-shop-tests")

fake = Faker()
