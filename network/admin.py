from django.contrib import admin
from .models import User, Post, Relationship
from django.contrib.auth.admin import UserAdmin


admin.site.register(Relationship)
admin.site.register(Post)
admin.site.register(User)
