from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
