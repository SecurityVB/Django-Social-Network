"""https://docs.djangoproject.com/en/5.0/topics/http/urls/"""

from django.contrib import admin
from django.urls import path, include
from blogs.views import page_not_found


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogs/', include('blogs.urls')),
    path('users/', include('users.urls', namespace="users")) # users:login
]


handler404 = page_not_found
admin.site.site_header = "Админ панель"
admin.site.index_title = "Блоги"