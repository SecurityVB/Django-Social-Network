from django.contrib import admin
from .models import BlogsLikes



@admin.register(BlogsLikes)
class BlogsLikesAdmin(admin.ModelAdmin):
    list_display = ("post", "liked_by", "time_create")
    ordering = ["-time_create"]
    search_fields = ["post", "liked_by"]