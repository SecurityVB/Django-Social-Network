from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Blogs.Status.PUBLISHED)


# class IncreasedPriorityManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(priority=Blogs.Priority.Increased)
#
#
# class NormalPriorityManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(priority=Blogs.Priority.Normal)




class Blogs(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, "Приватный"
        PUBLISHED = 1, "Общий Доступ"


    class Priority(models.IntegerChoices):
        Normal = 0, "Обычный"
        Increased = 1, "Повышенный"

    image = models.ImageField(upload_to="blogs/%Y/%m/%d", blank=True, null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, default=None, null=True)
    likes = models.IntegerField(blank=True, default=0)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.PUBLISHED)
    priority = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Priority.choices)),
                                       default=Priority.Normal)

    objects = models.Manager()
    published = PublishedManager()
    # increased_priority = IncreasedPriorityManager
    # normal_priority = NormalPriorityManager


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Blogs"
        ordering = ["-priority"]
    
    def get_absolute_url(self):
        return reverse("profiles", kwargs={"username": self.author.username})