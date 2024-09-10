from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index_view, name='index'),

    path('desk/', views.desk_view, name='desk'),
    path('desk/add_page/', views.AddPost.as_view(), name='add_page'),

    path('profile/', views.profile_view, name='profile'),
    path('profile/profile_settings/', views.ProfileSettingsUser.as_view(), name='profile_settings'),
    path('profiles/<slug:username>/', views.profiles_view, name='profiles'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)