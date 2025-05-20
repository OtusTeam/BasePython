from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # author = models.CharField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='posts')
    rating = models.IntegerField(default=0)
    tags = models.ManyToManyField('Tag', related_name='posts')

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    # author = models.CharField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class AuthorProfile(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField()
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return f'Profile for {self.author}'


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


