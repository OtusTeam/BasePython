from django.db import models
from django.contrib.auth import get_user_model

# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

UserModel: AbstractUser = get_user_model()


class UserProfile(models.Model):

    user = models.OneToOneField(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name="profile",
        related_query_name="profile",
    )
    bio = models.CharField(max_length=200)
    address = models.TextField(blank=True)

# class CustomUser(AbstractUser):
#     bio = models.CharField(...)


@receiver(post_save, sender=UserModel)
def toppings_changed(sender, instance: UserModel, created: bool = False, **kwargs):
    if created:
        profile = UserProfile.objects.create(user=instance)
