"""microblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api import views as api_views
from core import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path( 'api/post/', api_views.PostListCreateView.as_view(), name = 'api_post_list' ),
    path( 'api/users/', api_views.UserListView.as_view(), name = 'api_user_list' ),
    path( 'api/follows/', api_views.FollowListCreateView.as_view(), name = 'api_follow_list' ),
    path( 'api/post/<int:pk>/', api_views.PostRetrieveUpdateDestroyView.as_view(), name = 'api_post_list' ),
    path( 'api/follows/<str:username>/', api_views.FollowDestroyView.as_view(), name = 'api_follow' ),
    path('', views.index, name = 'home'),
    path('about', views.about, name = 'about'),
    path('post/<slug>/', views.post_detail, name = 'post_detail'),
]
