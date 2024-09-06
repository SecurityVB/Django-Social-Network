from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

import re


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Логин",
                              widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label="Пароль",
                              widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']



class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Логин",
                              widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label="Пароль",
                              widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label="Повтор пароля",
                               widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'city', 'password1', 'password2']
        labels = {
            'email': 'Почта',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'city': 'Город',
        }
        widgets = {
            'email': forms.PasswordInput(attrs={'class': 'form-input', 'type': 'email'}),
            'first_name': forms.PasswordInput(attrs={'class': 'form-input'}),
            'last_name': forms.PasswordInput(attrs={'class': 'form-input'}),
            'city': forms.PasswordInput(attrs={'class': 'form-input'}),
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Такой E-mail уже существует")
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if not bool(re.fullmatch(r'[a-z0-9]+', username)):
            raise forms.ValidationError("Логин не должен иметь заглавных букв или спец. символов")
        return username
