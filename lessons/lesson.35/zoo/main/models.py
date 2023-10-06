from django.db import models


class Animal(models.Model):
    name = models.CharField(verbose_name='Name', max_length=32)
    kind = models.TextField()
    age = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['pk']
        verbose_name = 'Zoo animal'
        verbose_name_plural = 'Zoo animals'
