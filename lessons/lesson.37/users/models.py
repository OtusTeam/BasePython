from django.contrib.auth.models import User, AbstractUser
from django.db import models


# Create your models here.
# extend
# class MyUserProfile(models.Model):
#     user = models.OneToOneField(
#         User,
#         on_delete=models.CASCADE,
#         primary_key=True,
#     )
#
#     # avatar = models.ImageField(upload_to='avatars', blank=True)
#     b_year = models.PositiveIntegerField(null=True)

class MyUser(AbstractUser):
    pass
    # date_joined = None
    email = models.EmailField('email address', unique=True)
    # # avatar = models.ImageField(upload_to='avatars', blank=True)
    b_year = models.PositiveIntegerField(null=True)
