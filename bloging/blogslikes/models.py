from django.contrib.auth import get_user_model
from django.db import models
from blogs.models import Blogs

class BlogsLikes(models.Model):
    post = models.ForeignKey(Blogs, on_delete=models.SET_NULL, default=None, null=True)
    liked_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    time_create = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return self.post.title

    class Meta:
        # unique_together = ('user', 'post')
        verbose_name_plural = "BlogsLikes"
