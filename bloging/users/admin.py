from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Bans


admin.site.register(User, UserAdmin)


@admin.register(Bans)
class BansAdmin(admin.ModelAdmin):
    list_display = ("user", "time_create", "cause")
    list_display_links = ("user",)
    ordering = ["-time_create"]
    list_filter = ["time_create"]
