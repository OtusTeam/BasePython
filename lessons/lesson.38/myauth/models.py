from django.contrib.auth.models import AbstractUser, User
from django.db import models


# class OtusUser(AbstractUser):
#     user = models.OneToOneField(
#         User,
#         primary_key=True,
#         on_delete=models.CASCADE,
#     )
#     bio = models.TextField('biography', blank=True)


class OtusUser(AbstractUser):
    # date_joined = None
    # email = models.EmailField('email address', unique=True)
    bio = models.TextField('biography', blank=True)
