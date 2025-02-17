from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import login


import random
# Create your views here.
def index(request):
    films = Kino.objects.all()
    artists = Artist.objects.all()
    print(films)
    print(artists)
    randomFilm = random.choice(films)
    data = {'randomFilm': randomFilm,'films':films,'artists':artists}
    return render(request, 'index.html',data)

from django.views import generic
class kinoList(generic.ListView):
    model = Kino
    paginate_by = 1

class artistList(generic.ListView):
    model = Artist

class kinoDetail(generic.DetailView):
    model = Kino

def registration(request):
    if request.POST:#нажали на кнопку отправить
        print(1)
        form = UserForm(request.POST)#видим заполненную форму
        if form.is_valid():#проверка формы на корректность
            print(2)
            k1 = form.cleaned_data['username']#собираем данные
            k2 = form.cleaned_data['email']
            k3 = form.cleaned_data['password1']
            k4 = form.cleaned_data['first_name']
            k5 = form.cleaned_data['last_name']
            User.objects.create_user(username=k1,email=k2,password=k3)#создает записть в таблице user
            myuser = User.objects.get(username=k1)#находим нового пользователя
            myuser.first_name = k4#Добавляем имя
            myuser.last_name = k5
            myuser.save()#сохраняем таблицу
            Profile.objects.create(user=myuser)#создает запись в таблице профиль
            login(request,myuser)#автовход на сайт
            return redirect('index')

    else:
        form = UserForm()#форма регистрации
    data = {'form':form}
    return render(request,'registration/reg.html',data)

def profile(request):
    return render(request,'kabinet.html')

def profileChange(request):
    form = ProfileForm()
    data = {'form':form}
    if request.POST:
        k1 = request.POST['newpodpiska']
        user = User.objects.get(id = request.user.id)
        user.profile.podpiska_id = k1
        user.profile.save()
        return redirect('kabinet')
    return render(request,'kabinet.html',data)

