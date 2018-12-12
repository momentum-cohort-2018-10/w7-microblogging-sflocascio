from django.shortcuts import render
from core.models import Post
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from api.serializers import PostSerializer

#Serialization convert json to objects and objects to json 

@api_view(["GET"])
def post_list(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)