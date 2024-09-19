"""https://docs.djangoproject.com/en/5.0/topics/http/urls/"""

from django.contrib import admin
from django.urls import path, include
from blogs.views import page_not_found

from . import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogs/', include('blogs.urls')),
    path('users/', include('users.urls', namespace="users")), # users:login
    path('blogslikes/', include('blogslikes.urls', namespace="blogslikes")), # users:login
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = page_not_found
admin.site.site_header = "Админ панель"
admin.site.index_title = "Блоги"

