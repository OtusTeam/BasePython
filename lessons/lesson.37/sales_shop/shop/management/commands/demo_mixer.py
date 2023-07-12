from django.core.management import BaseCommand
from mixer.backend.django import mixer

from shop.models import Category, Product


from sales_shop.fake import fake


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Start mixer")

        category = mixer.blend(Category)
        print(category)

        categories = mixer.cycle(3).blend(
            Category,
            name=fake.word,
            # name=mixer.FAKE,
            archived=True,
        )
        print(categories)

        products = mixer.cycle(3).blend(
            Product,
            name=fake.sentence,
            price=lambda: fake.pydecimal(min_value=0, max_value=10000),
            category=mixer.SELECT,
        )
        print(products)
