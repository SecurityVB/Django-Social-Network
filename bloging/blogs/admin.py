from django.contrib import admin
from .models import Blogs #, Profiles

@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "time_create", "count_content", "is_published", "priority") # "profile_id",
    list_display_links = ("id",)
    ordering = ["-time_create"]
    list_editable = ("is_published", "title", "priority")
    actions = ["set_published", "set_draft", "increase_priority", "lower_priority"]
    search_fields = ["title", "author__startswith"]
    list_filter = ["is_published", "priority"] # "profile_id__city",


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



# @admin.register(Profiles)
# class ProfilesAdmin(admin.ModelAdmin):
#     list_display = ("id", "full_name", "city", "back_path", "icon_path")
#     list_display_links = ("id", "full_name")