from django.shortcuts import render
from core.models import Post, Follow, User
from rest_framework.response import Response 
from api.serializers import PostSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework import generics


#Serialization convert json to objects and objects to json 

class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return self.request.user.posts

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

# class FollowListCreateView(generics.ListCreateAPIView):
#     serializer_class = FollowSerializer

#     def get_queryset(self):
#         return self.request.user.follows_from

#     def perform_create(self, serializer):
#         serializer.save(following_user=self.request.user)

       

# class PostListCreateView(APIView):
#     def get(self, request):
#         posts = Post.objects.filter(owner=request.user)
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)

#     def post(self, rquest):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(owner=request.user)
#             return Response(serializer.data, status=201)

#         return Response(serializer.errors, status=400)






# @api_view(["GET"])
# def post_list(request):
#     posts = Post.objects.all()
#     serializer = PostSerializer(posts, many=True)
#     return Response(serializer.data)


