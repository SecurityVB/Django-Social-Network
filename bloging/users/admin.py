from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Bans


admin.site.register(User, UserAdmin)


@admin.register(Bans)
class BansAdmin(admin.ModelAdmin):
    list_display = ("user", "ban", "count_cause", "time_create", "time_update")
    list_display_links = ("user",)
    ordering = ["-time_update"]
    list_editable = ("ban",)
    actions = ["ban", "unban"]
    search_fields = ["count_cause"]
    list_filter = ["ban"]

    @admin.display(description="symbols", ordering='cause')
    def count_cause(self, bans: Bans):
        return f"{len(bans.cause)} символов"

    @admin.action(description="Забанить выбранных пользователей")
    def ban(self, request, queryset):
        count = queryset.update(ban=Bans.Status.Ban)
        self.message_user(request, f"{count} пользователей забанено.")

    @admin.action(description="Разбанить выбранных пользователей")
    def ban(self, request, queryset):
        count = queryset.update(is_published=Bans.Status.Unban)
        self.message_user(request, f"{count} пользователей разбанено.")
