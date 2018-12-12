from django.shortcuts import render
from core.models import Post
from rest_framework.decorators import api_view
from rest_framework.response import Response 

#Serialization convert json to objects and objects to json 

@api_view(["GET"])
def post_list(request):
    posts = Post.objects.all()
    post_data = [
        {"id": p.id, "title": p.title, "author": p.author} for p in posts 
    ]
    return Response(post_data)