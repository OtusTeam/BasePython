from django.db import models
from django.shortcuts import reverse


class Task(models.Model):

    class Meta:
        ordering = ("id", )

    title = models.CharField(max_length=200, default="", null=False)
    description = models.TextField(default="", db_default="", blank=True)
    done = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("tasks:detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title
