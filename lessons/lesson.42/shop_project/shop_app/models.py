from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Category(models.Model):
    """
    Категории товаров:

    - продукты
    - стройматериалы
    - канцелярские товары
    - и так далее
    """

    class Meta:
        ordering = "pk",
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=80)
    description = models.TextField(null=False, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):

    class Meta:
        ordering = "pk",

    title = models.CharField(max_length=100)
    description = models.TextField(null=False, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    archived = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class Order(models.Model):
    address = models.CharField(max_length=300)
    comment = models.CharField(max_length=100, blank=True)
    promocode = models.CharField(max_length=50, blank=True)
    products = models.ManyToManyField(
        Product,
        through="OrderProduct",
        through_fields=("order", "product"),
        related_name="orders",
    )
    user = models.ForeignKey(User, on_delete=models.PROTECT)


class OrderProduct(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="order_products",
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="order_products",
    )
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
