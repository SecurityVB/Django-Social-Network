from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.fields import return_None
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, get_object_or_404, get_list_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import UpdateView, FormView

from .forms import ProfileSettingsForm, AddPostForm

from .models import Blogs # , Profiles, UploadFiles
from django.contrib.auth.decorators import login_required


"""----------------------------INDEX---------------------------"""

@login_required()
def index_view(request):
    return HttpResponseRedirect(reverse("desk"))


"""___________________DESK____________________________________"""


@login_required()
def desk_view(request):
    posts_increased = Blogs.published.filter(priority=Blogs.Priority.Increased)
    posts_normal = Blogs.published.filter(priority=Blogs.Priority.Normal)
    data = {
        "title": "Главная",
        "Increased": posts_increased,
        "Normal": posts_normal,
    }
    return render(request, 'blogs/desk.html', data)



class AddPost(LoginRequiredMixin, FormView):
    form_class = AddPostForm
    template_name = 'blogs/add_page.html'

    def form_valid(self, form):
        blog_post = form.save(commit=False)
        blog_post.author = self.request.user
        blog_post.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('desk')

    # extra_context = {
    #     "default_icon": settings.DEFAULT_USER_ICON,
    #     "default_back": settings.DEFAULT_USER_BACK,
    # }



"""___________________PROFILE____________________________________"""



@login_required()
def profile_view(request):
    return render(request, 'blogs/profile.html')



class ProfileSettingsUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileSettingsForm
    template_name = 'blogs/profile_settings.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('profile')

    # extra_context = {
    #     "default_icon": settings.DEFAULT_USER_ICON,
    #     "default_back": settings.DEFAULT_USER_BACK,
    # }





@login_required()
def profiles_view(request, username):
    user = get_user_model().objects.get(username=username)
    data = {
        "profile": user,
    }
    return render(request, 'blogs/profiles.html', data)


"""----------------------------OTHER---------------------------"""


def page_not_found(request, exception):
    return render(request, 'blogs/not_found_404.html', {"title": "Страница не найдена"})