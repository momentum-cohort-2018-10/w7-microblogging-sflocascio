from django.contrib import admin
from django.contrib.auth.models import AbstractUser
from core.models import Post 

class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('title', 'link', 'description')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)