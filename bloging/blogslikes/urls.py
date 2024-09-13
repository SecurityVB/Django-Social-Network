from django.urls import path
from . import views


app_name = "blogslikes"

urlpatterns = [
    path('like/<int:post_id>', views.likes, name='like'),
]