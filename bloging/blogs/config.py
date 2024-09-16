from django.contrib.auth import logout
from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from users.models import Bans



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
    """Миксин для проверки бана при выходе пользователя"""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            # Если пользователь не аутентифицирован, перенаправляем его на логин
            return redirect('users:login')

        try:
            # Проверяем, забанен ли пользователь
            ban_status = Bans.objects.get(user=request.user).ban
        except Bans.DoesNotExist:
            ban_status = False  # Если нет записи в Bans, считаем, что пользователь не забанен

        if ban_status:
            # Если пользователь забанен, перенаправляем его на логин или другую страницу
            return redirect('users:login')

        # Если всё хорошо, продолжаем выполнение LogoutView
        return super().dispatch(request, *args, **kwargs)



def ban_required(view_func):
    def wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('users:login')

        try:
            # Проверяем, забанен ли пользователь
            ban = Bans.objects.get(user=request.user).ban
        except Bans.DoesNotExist:
            ban = False

        if ban:
            # Если пользователь забанен, перенаправляем на логин
            return redirect('users:login')

        # Выполняем логику выхода
        logout(request)
        return view_func(request, *args, **kwargs)

    return wrapped_view