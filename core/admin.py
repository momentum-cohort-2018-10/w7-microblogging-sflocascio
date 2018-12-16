from django.contrib import admin
from django.contrib.auth.models import AbstractUser
from core.models import User, Post, Follow

class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('title', 'link', 'description')
    prepopulated_fields = {'slug': ('title',)}

class FollowersInline(admin.StackedInline):
    model = Follow
    fk_name = "followed_user"
    fields = ("following_user",)
    extra = 1 

class UserAdmin(admin.ModelAdmin):
    fields = ("username", 'email', 'is_superuser', 'is_staff', 'is_active')
    inlines = [FollowersInline]

admin.site.register(Post, PostAdmin)
admin.site.register(User, UserAdmin)