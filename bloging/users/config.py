from django.contrib.auth import logout
from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Bans



# def ban_required(view_func):
#     @login_required
#     def wrapped_view(request, *args, **kwargs):
#         try:
#             ban = Bans.objects.get(user=request.user).ban
#         except Bans.DoesNotExist:
#             ban = False
#
#         if ban:
#             return redirect('users:logout')
#
#         return view_func(request, *args, **kwargs)
#
#     return wrapped_view
#
#
# class BanLoginRequiredMixin(LoginRequiredMixin):
#     def dispatch(self, request, *args, **kwargs):
#         if not request.user.is_authenticated:
#             return redirect('users:login')
#
#         try:
#             ban_status = Bans.objects.get(user=request.user).ban
#         except Bans.DoesNotExist:
#             ban_status = False
#
#         if ban_status:
#             return redirect('users:login')
#
#         return super().dispatch(request, *args, **kwargs)


class BanLoginRequiredMixin(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('users:login')

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