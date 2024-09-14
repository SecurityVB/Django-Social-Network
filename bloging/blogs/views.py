from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.conf import settings
from django.views.generic import UpdateView, FormView
from django.contrib.auth.decorators import login_required

from .forms import ProfileSettingsForm, AddPostForm

from blogslikes.models import BlogsLikes
from .models import Blogs




"""----------------------------INDEX---------------------------"""

@login_required()
def index_view(request):
    return HttpResponseRedirect(reverse("desk"))


"""___________________DESK____________________________________"""


@login_required()
def desk_view(request):
    blogs = Blogs.published.all()

    data = {
        "title": "Главная",
        "blogs": blogs,
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

    extra_context = {
        "default_icon": settings.DEFAULT_USER_ICON,
        "default_back": settings.DEFAULT_USER_BACK,
    }



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

    extra_context = {
        "default_icon": settings.DEFAULT_USER_ICON,
        "default_back": settings.DEFAULT_USER_BACK,
    }





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