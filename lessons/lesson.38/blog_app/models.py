from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='posts')
    rating = models.IntegerField(default=0)
    tags = models.ManyToManyField('Tag', related_name='posts')

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='comments')
    created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f'Комментарий by {self.author}'


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class AuthorProfile(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField()
    website = models.URLField(blank=True, null=True)


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
