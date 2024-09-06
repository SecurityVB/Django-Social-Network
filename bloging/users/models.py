from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    icon = models.ImageField(upload_to="users/icon/%Y/%m/%d", blank=True, null=True)
    back = models.ImageField(upload_to="users/back/%Y/%m/%d", blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    date_birth = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)