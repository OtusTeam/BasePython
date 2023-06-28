from django.contrib.auth import get_user_model
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

from .tasks import notify_order_saved


class Category(models.Model):

    class Meta:
        # verbose_name = "Category"
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Status(models.IntegerChoices):
        ARCHIVED = 0
        AVAILABLE = 1

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="products",
    )
    status = models.IntegerField(
        choices=Status.choices,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Product <{self.pk}, {self.name!r}>"


class Order(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
    )
    products = models.ManyToManyField(
        Product,
        related_name="orders",
    )
    address = models.TextField()
    promocode = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OrderPaymentDetails(models.Model):
    class Meta:
        verbose_name_plural = "Order Payment Details"

    class Status(models.IntegerChoices):
        PENDING = 0
        CONFIRMED = 1

    order = models.OneToOneField(
        Order,
        on_delete=models.CASCADE,
        related_name="payment_details",
    )
    payed_at = models.DateTimeField(
        blank=True,
        null=True,
    )
    card_ends_with = models.CharField(max_length=5, blank=True)
    status = models.IntegerField(
        choices=Status.choices,
        default=Status.PENDING,
    )


# def on_order_create_add_payment_details
@receiver(post_save, sender=Order)
def on_order_save(instance: Order, created: bool, **kwargs):
    """
    Argument	Value

    sender
    The model class.

    instance
    The actual instance being saved.

    created
    A boolean; True if a new record was created.

    raw
    A boolean; True if the model is saved exactly as presented (i.e. when loading a fixture). One should not query/modify other records in the database as the database might not be in a consistent state yet.

    using
    The database alias being used.

    update_fields
    The set of fields to update as passed to Model.save(), or None if update_fields wasn’t passed to save().

    :return:
    """

    notify_order_saved.delay(
        order_pk=instance.pk,
        promocode=instance.promocode,
    )

    if not created:
        return

    OrderPaymentDetails.objects.get_or_create(
        order=instance,
    )
