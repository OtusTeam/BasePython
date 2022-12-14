from django.db import models


class Animal(models.Model):
    kind = models.CharField('kind', max_length=64)
    age = models.IntegerField(verbose_name='age')
    desc = models.TextField(verbose_name='description', blank=True)

    def __str__(self):
        return f'{self.kind} ({self.age})'

    # class Meta:
    #     verbose_name = 'animal'
    #     verbose_name_plural = 'animals'
    #     ordering = ['pk']
