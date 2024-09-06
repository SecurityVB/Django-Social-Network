from datetime import datetime
from django import forms
from django.contrib.auth import get_user_model

from .models import Blogs




class AddPostForm(forms.ModelForm):

    class Meta:
        model = Blogs
        fields = ["title", "content", "is_published", "priority"]
        widgets = {
            'title': forms.TextInput(),
            'content': forms.Textarea(),
        }
        labels = {"title": "Заголовок", "content": "Содержимое",
                  "is_published": "В общий доступ",
                  "priority": "Повышенный приоритет",
                  }



class ProfileSettingsForm(forms.ModelForm):
    username = forms.CharField(required=False, disabled=True, label="Логин", widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.CharField(required=False, disabled=True, label="Почта", widget=forms.TextInput(attrs={'class': 'form-input'}))

    this_year = datetime.now().year
    date_birth = forms.DateField(label="Дата рождения", widget=forms.SelectDateWidget(years=tuple(range(this_year - 100, this_year - 12))))

    class Meta(forms.ModelForm):
        model = get_user_model()
        fields = ['icon', 'back', 'first_name', 'last_name', 'date_birth', 'city', 'description', 'username', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
            'city': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.TextInput(attrs={'class': 'form-input'}),
        }
        labels = {
            'icon': 'Аватарка',
            'back': 'Задний фон',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'city': 'Город',
            'description': 'О себе',
        }
