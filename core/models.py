from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Timestamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(Timestamp):
    title = models.CharField(max_length=255)
    link = models.URLField(null=True, blank=True)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, max_length=255)
    likes = models.IntegerField(null=True)

    def __str__(self):
        return self.title



# class Follow(models.model):
#     following_user = models.models.ForeignKey(User, on_delete=models.CASCADE)
#     followed_user = models.models.ForeignKey(User, on_delete=models.CASCADE)