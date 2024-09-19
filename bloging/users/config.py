from django.contrib.auth import logout
from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Bans



class BanLoginRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        try:
            ban = Bans.objects.get(user=request.user)
        except Bans.DoesNotExist:
            ban = False

        if ban:
            return redirect('users:login')

        return super().dispatch(request, *args, **kwargs)



def ban_required(view_func):
    def wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('users:login')

        try:
            ban = Bans.objects.get(user=request.user)
        except Bans.DoesNotExist:
            ban = False

        if ban:
            logout(request)
            return redirect('users:login')


        return view_func(request, *args, **kwargs)

    return wrapped_view