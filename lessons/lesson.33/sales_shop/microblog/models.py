from typing import Type

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models

from shop.models import Product


AuthUser: Type[AbstractUser] = get_user_model()


class Article(models.Model):
    author = models.ForeignKey(
        AuthUser,
        on_delete=models.PROTECT,
    )
    title = models.CharField(max_length=100)
    text = models.TextField()
    products = models.ManyToManyField(
        Product,
        related_name="articles",
    )


