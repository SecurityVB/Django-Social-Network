from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    icon = models.ImageField(upload_to="users/icon/%Y/%m/%d", blank=True, null=True)
    back = models.ImageField(upload_to="users/back/%Y/%m/%d", blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    date_birth = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)


class Bans(models.Model):
    class Status(models.IntegerChoices):
        Ban = 1, "Забанен"
        Unban = 0, "Разбанен"

    user = models.OneToOneField(get_user_model(), on_delete = models.CASCADE, primary_key = True)
    ban = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                              default=Status.Ban)
    cause = models.CharField(max_length=1000, blank=True, null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = "Bans"
        ordering = ["-time_update"]
