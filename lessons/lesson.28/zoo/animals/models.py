from django.db import models


class Animal(models.Model):
    name = models.CharField(max_length=64)
    kind = models.TextField()
    age = models.PositiveSmallIntegerField(null=True)

    def __str__(self):
        return f'{self.name} <{self.kind}>'

    class Meta:
        verbose_name = 'животное'
        verbose_name_plural = 'животные'
