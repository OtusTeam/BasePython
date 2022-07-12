from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


# class MyCustomUser(AbstractUser):
#     lang = models.CharField(max_length=2)

class UserDemo(models.Model):
    lang = models.CharField(max_length=2)
    name = models.CharField(max_length=32)
    birth_dt = models.DateField()
    birth_month = models.IntegerField(
        db_index=True,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(12),
        ]
    )


class Employee(UserDemo):
    internal_id = models.PositiveSmallIntegerField()
    internal_email = models.EmailField()


class Order(models.Model):

    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        AWAITING_SHIPMENT = 'awaiting_shipment', 'Awaiting Shipment'
        SHIPPED = 'shipped', 'Shipped'
        DELIVERED = 'delivered', 'Delivered'

    status = models.CharField(
        max_length=30,
        choices=Status.choices,
        default=Status.PENDING,
    )
    shipped_on = models.DateTimeField(null=True, blank=True)
    shipped_by = models.ForeignKey(Employee, on_delete=models.PROTECT, null=True, blank=True)
    delivered_on = models.DateTimeField(null=True, blank=True)


UserModel: AbstractUser = get_user_model()
# UserModel = MyCustomUser


class UserProfile(models.Model):
    # user = models.OneToOneField('myauth.MyCustomUser')
    # user = models.OneToOneField(settings.AUTH_USER_MODEL)
    user = models.OneToOneField(
        UserModel,
        primary_key=True,
        on_delete=models.CASCADE,
    )
    bio = models.TextField(null=False, blank=True)


@receiver(post_save, sender=UserModel)
def user_saved_handler(instance: UserModel, created: bool, **kwargs):
    # print("instance", instance, "created?", created)
    if not created:
        return

    UserProfile.objects.create(user=instance)
