from django.core.management.base import BaseCommand

import factory
from django.utils import timezone
from factory.django import DjangoModelFactory
from faker import Faker

from myauth.models import Order

fake = Faker()


class UserDemoFactory(DjangoModelFactory):
    class Meta:
        model = "myauth.UserDemo"

    lang = factory.Iterator(["en", "ru", "fr", "de", "es"])
    name = factory.Faker("name")
    birth_dt = factory.Faker("date_of_birth")
    birth_month = factory.SelfAttribute("birth_dt.month")


class EmployeeFactory(UserDemoFactory):
    class Meta:
        model = "myauth.Employee"

    # internal_id = factory.Faker("pyint", min_value=10, max_value=100)
    internal_id = factory.Sequence(int)
    internal_email = factory.LazyAttribute(
        lambda o: "{name}.{internal_id:03d}@{domain}".format(
            name=fake.user_name(),
            internal_id=o.internal_id,
            domain=fake.domain_name(),
        )
    )


class OrderFactory(DjangoModelFactory):
    class Meta:
        model = Order

    status = factory.Iterator(Order.Status.values[:2])
    # status = factory.Iterator(Order.Status.choices[:2], getter=lambda s: s[0])
    shipped_on = None
    shipped_by = None
    delivered_on = None

    class Params:
        shipped = factory.Trait(
            status=Order.Status.SHIPPED,
            shipped_on=factory.Faker(
                "date_time_between",
                start_date="-3M",
                end_date="-1M",
                tzinfo=timezone.utc,
            ),
            shipped_by=factory.SubFactory(EmployeeFactory),
        )
        delivered = factory.Trait(
            status=Order.Status.DELIVERED,
            shipped_on=factory.Faker(
                "date_time_between",
                start_date="-3M",
                end_date="-1M",
                tzinfo=timezone.utc,
            ),
            shipped_by=factory.SubFactory(EmployeeFactory),
            delivered_on=factory.Faker(
                "date_time_between",
                start_date="-25d",
                tzinfo=timezone.utc,
            ),

        )


def demo_users_and_emp():
    user = UserDemoFactory.build()
    print(user)
    print(vars(user))

    # users = UserDemoFactory.build_batch(6)
    # for user in users:
    #     print(user)
    #     print(vars(user))

    employee = EmployeeFactory.build()
    print(employee)
    print(vars(employee))

    employees = EmployeeFactory.build_batch(7)
    for employee in employees:
        print(employee.internal_email)


class Command(BaseCommand):
    def handle(self, *args, **options):
        # demo_users_and_emp()
        orders = OrderFactory.build_batch(3)
        for order in orders:
            print(order.status)

        order = OrderFactory.create(shipped=True)
        print(order)
        print(order.status)
        print(order.shipped_on)
        print(order.shipped_by)
        print(vars(order.shipped_by))
        order = OrderFactory.create(delivered=True)
        print("===" * 3)

        print(order)
        print(order.status)
        print("shipped:", order.shipped_on)
        print("delivered:", order.delivered_on)
        print(order.shipped_by)
        print(vars(order.shipped_by))

