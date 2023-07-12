from datetime import datetime

from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from django.utils import timezone

import factory
from django.db.models.signals import post_save
from factory.django import DjangoModelFactory

from shop.models import Category, Product, Order, OrderPaymentDetails


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category
        django_get_or_create = ("name", )

    name = factory.Faker("word")
    description = factory.Faker("sentence", nb_words=7)
    archived = False


class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker("word")
    price = factory.Faker("pydecimal", min_value=0, max_value=10000)
    # description = factory.Faker("paragraph")
    description = factory.LazyAttribute(lambda o: f"Product {o.name} of category {o.category.name}")
    category = factory.SubFactory(CategoryFactory)
    status = factory.Iterator(Product.Status.values)


class OrderPaymentDetailsFactory(DjangoModelFactory):
    class Meta:
        model = OrderPaymentDetails


@factory.django.mute_signals(post_save)
class OrderFactory(DjangoModelFactory):
    class Meta:
        model = Order

    user = factory.Iterator(get_user_model().objects.all())
    # products = factory.Iterator(Product.objects.all())
    address = factory.Faker("address")
    promocode = factory.Faker("word")
    payment_details = factory.RelatedFactory(
        OrderPaymentDetailsFactory,
        factory_related_name="order",
        # payed_at=factory.LazyFunction(datetime.utcnow)
        # payed_at=factory.LazyFunction(timezone.now)
    )

    @factory.post_generation
    def products(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for product in extracted:
                self.products.add(product)

    class Params:
        empty_address = factory.Trait(
            address="",
            payment_details=None,
        )
        paid = factory.Trait(
            payment_details__card_ends_with=factory.Faker("word"),
            payment_details__payed_at=factory.LazyFunction(timezone.now),
        )
        paid_confirmed = factory.Trait(
            payment_details__card_ends_with=factory.Faker("word"),
            payment_details__status=OrderPaymentDetails.Status.CONFIRMED,
            payment_details__payed_at=factory.LazyFunction(timezone.now),
        )


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Start factory boy")

        # category = CategoryFactory()
        # print(category)
        # category = CategoryFactory.create()
        category = CategoryFactory.build()
        print(category, category.pk)

        categories = CategoryFactory.build_batch(
            16,
            name=factory.Iterator(["foo", "bar", "spam", "eggs"]),
        )
        print(categories)

        # categories = CategoryFactory.create_batch(2)
        # print(categories)

        # category = CategoryFactory(
        #     description=factory.Faker("paragraph"),
        #     archived=True,
        # )
        # print(category)

        # product = ProductFactory()
        # print(product)
        # print(product.category)

        # order = OrderFactory.build()
        # order = OrderFactory.create(
        #     # paid_confirmed=True,
        #     # products=Product.objects.all()[:4],
        # )
        # print(order)
        # print(order.payment_details)

        order = OrderFactory.build(empty_address=True)
        print(order, [order.address])
