from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    bio = models.TextField()

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)
    viwes_count = models.IntegerField(default=0)
    category = models.CharField(max_length=100)
    published_date = models.DateField()

    def __str__(self):
        return self.title