from django.apps import AppConfig


class BlogsConfig(AppConfig):
    verbose_name = "Посты"
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blogs'

