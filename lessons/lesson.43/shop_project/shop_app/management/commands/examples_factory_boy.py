from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
import factory
from django.db.models.signals import post_save

from datetime import timezone
from factory.django import DjangoModelFactory

from shop_app.models import Category, Product, Order, OrderProduct


UserModel = get_user_model()


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker("word")
    description = factory.Faker("sentence")


class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    title = factory.Faker("sentence", nb_words=3)
    description = factory.Faker("sentence")
    price = factory.Faker(
        "pydecimal",
        left_digits=4,
        right_digits=2,
        positive=True,
    )
    archived = False
    category = factory.Iterator(Category.objects.all())
    # category = factory.SubFactory(CategoryFactory)


@factory.django.mute_signals(post_save)
class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Order

    address = factory.Faker("address")
    comment = factory.Faker("sentence")
    promocode = factory.Faker("word")

    user = factory.Iterator(UserModel.objects.all())

    # @factory.post_generation
    # def products(self, create, extracted, **kwargs):
    #     if not create or not extracted:
    #         # Simple build, or nothing to add, do nothing.
    #         return
    #
    #     # Add the iterable of groups using bulk addition
    #     self.products.add(*extracted)

    class Params:
        shipped = factory.Trait(
            status=Order.Status.SHIPPED,
            shipped_at=factory.Faker(
                "date_time_between",
                start_date="-1w",
                end_date="-1d",
                tzinfo=timezone.utc,
            ),
        )
        delivered = factory.Trait(
            status=Order.Status.DELIVERED,
            shipped_at=factory.Faker(
                "date_time_between",
                start_date="-1M",
                end_date="-1w",
                tzinfo=timezone.utc,
            ),
        )


class OrderProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = OrderProduct

    order = factory.SubFactory(OrderFactory)
    product = factory.SubFactory(ProductFactory)
    quantity = factory.Faker(
        "pyint",
        min_value=1,
        max_value=10,
    )
    price = factory.Faker(
        "pydecimal",
        left_digits=4,
        right_digits=2,
        positive=True,
    )


class OrderWithProductFactory(OrderFactory):
    order_product = factory.RelatedFactory(
        OrderProductFactory,
        factory_related_name="order",
    )


class OrderWithTwoProductsFactory(OrderFactory):
    order_product1 = factory.RelatedFactory(
        OrderProductFactory,
        factory_related_name="order",
    )
    order_product2 = factory.RelatedFactory(
        OrderProductFactory,
        factory_related_name="order",
    )


class Command(BaseCommand):
    help = "Factory Boy Examples"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Show Factory Boy Examples"))

        new_category = CategoryFactory()
        self.stdout.write(self.style.SUCCESS(f"Category {new_category!r} created"))

        product = ProductFactory()
        self.stdout.write(
            self.style.SUCCESS(
                f"Product {product!r} with category {product.category!r} created",
            )
        )

        products = ProductFactory.create_batch(10)
        for product in products:
            self.stdout.write(
                self.style.SUCCESS(
                    f"Product {product!r} with category {product.category!r} created",
                )
            )

        order1 = OrderWithProductFactory()
        order2 = OrderWithTwoProductsFactory()

        for order in (order1, order2):
            print("Order:", order)
            for product in order.products.all():
                print("- Product:", product)

        product_with_new_category = ProductFactory(
            category=factory.SubFactory(CategoryFactory),
            # title=factory.Faker("sentence"),
        )
        self.stdout.write(
            self.style.SUCCESS(
                f"New Product {product_with_new_category!r} with new category {product_with_new_category.category!r} created",
            ),
        )

        product_with_new_category = ProductFactory.create_batch(
            # how many to create
            10,
            # new for each product:
            # category=factory.SubFactory(CategoryFactory),
            # same for all products
            # category=CategoryFactory(),
        )

        order_1 = OrderWithProductFactory(shipped=True)
        order_2 = OrderWithProductFactory(delivered=True)

        order_3 = OrderWithTwoProductsFactory(shipped=True)
        order_4 = OrderWithTwoProductsFactory(delivered=True)

        for order in (
            order_1,
            order_2,
            order_3,
            order_4,
        ):
            print(
                "Order:",
                order,
                "status:",
                order.status,
                "shipped_at:",
                order.shipped_at,
            )
            for product in order.products.all():
                print("- Product:", product)

        self.stdout.write(self.style.SUCCESS("Done"))
