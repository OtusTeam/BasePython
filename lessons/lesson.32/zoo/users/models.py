from django.db import models
from django.contrib.auth.models import User, Group, AbstractUser


# Create your models here.
class MyUser(AbstractUser):
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField(default=18)
