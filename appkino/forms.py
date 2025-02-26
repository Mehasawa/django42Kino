from cProfile import label

from django import forms
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import CaptchaField
from .models import *


class UserForm(UserCreationForm):
    username = forms.CharField(label='Login',
                               help_text='')
    password1 = forms.CharField(label='Пароль',
                    help_text='',
                    widget=forms.PasswordInput(
                        attrs={'autocomplete':'new-password'}
                    ))
    password2 = forms.CharField(label='Подтверждение',
                    help_text='',
                    widget=forms.PasswordInput(
                        attrs={'autocomplete':'new-password'}
                    ))
    email = forms.EmailField(label='Почта',
                    widget=forms.TextInput(
                        attrs={'placeholder':'qwe@mail.ru'}))
    first_name = forms.CharField(label='Имя', required=False)
    last_name = forms.CharField(label='Фамилия', required=False)
    captcha = CaptchaField()


class ProfileForm(forms.Form):
    newpodpiska = forms.ModelChoiceField(queryset=Podpiska.objects.all(),
                                         label='Выберите подписку')

class KinoForm(forms.Form):
    genre = forms.ModelChoiceField(queryset=Genre.objects.all(),
                                   required=False, label='Жанр')
    director = forms.ModelChoiceField(queryset=Director.objects.all(),
                                      required=False, label='Режиссер')
    title = forms.CharField(required=False, label='Название')

class OtzivForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs= {'name': 'text','rows':5,'cols':50})
                           ,label='напишите отзыв', min_length=10)
    nerobot = forms.BooleanField(label='Вы не робот')