from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='posts')
    rating = models.IntegerField(default=0)

    tags = models.ManyToManyField('Tag', related_name='posts')
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    # author = models.CharField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments') # post.comments.all()

    def __str__(self):
        return f"{self.author}'s comment"


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class AuthorProfile(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField()
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"Profile of {self.author.name}"


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


