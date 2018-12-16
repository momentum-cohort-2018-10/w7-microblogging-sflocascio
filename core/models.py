from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    users_followed = models.ManyToManyField(
        to="User",
        through="Follow",
        through_fields=("following_user", "followed_user"),
        related_name="followers",
    )

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



class Follow(models.Model):
    following_user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name="follows_from")
    followed_user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name="follows_to")
    created_at = models.DateTimeField(auto_now_add=True, null=True)