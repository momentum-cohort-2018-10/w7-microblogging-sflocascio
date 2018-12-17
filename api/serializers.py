from rest_framework import serializers
from core.models import Post, User, Follow

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "title", "author", "description")

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username",)




