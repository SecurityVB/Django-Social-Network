from django.contrib import admin
from .models import Blogs
from blogslikes.models import BlogsLikes



@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "time_create", "count_content", "likes", "is_published", "priority") # "profile_id",
    list_display_links = ("id",)
    ordering = ["-time_create"]
    list_editable = ("is_published", "title", "priority")
    actions = ["set_published", "set_draft", "increase_priority", "lower_priority", "remove_likes"]
    search_fields = ["title", "author__startswith"]
    list_filter = ["is_published", "priority", "likes"]


    @admin.display(description="symbols", ordering='content') # Название поля функции и сортировка
    def count_content(self, blogs: Blogs):
        return f"{len(blogs.content)} символов"


    @admin.action(description="Опубликовать выбраннные записи")
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Blogs.Status.PUBLISHED)
        self.message_user(request, f"Опубликовано {count} записей.")


    @admin.action(description="Сделать приватными выбранные записи")
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Blogs.Status.DRAFT)
        self.message_user(request, f"{count} записей сняты с общего доступа.")


    @admin.action(description="Повысить приоритет")
    def increase_priority(self, request, queryset):
        count = queryset.update(priority=Blogs.Priority.Increased)
        self.message_user(request, f"У {count} записей повышен приоритет.")


    @admin.action(description="Понизить приоритет")
    def lower_priority(self, request, queryset):
        count = queryset.update(priority=Blogs.Priority.Normal)
        self.message_user(request, f"У {count} записей понижен приоритет.")


    @admin.action(description="Убрать лайки с постов")
    def remove_likes(self, request, queryset):
        queryset.update(likes=0)

        for blog in queryset:
            BlogsLikes.objects.filter(post=blog).delete()

        count = queryset.update(priority=Blogs.Priority.Increased)
        self.message_user(request, f"У {count} записей убраны лайки.")