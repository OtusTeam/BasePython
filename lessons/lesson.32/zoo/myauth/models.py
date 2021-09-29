from django.contrib.auth.models import User, AbstractUser
from django.db import models


# class MyUserInfo(models.Model):
#     user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
#     age = models.PositiveSmallIntegerField(default=18)
#     # avatar = ...


class MyUser(AbstractUser):
    age = models.PositiveSmallIntegerField(default=18)
    email = models.EmailField(unique=True)
    # first_name = None
