from django.shortcuts import render
from .models import *
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

class artistList(generic.ListView):
    model = Artist

class kinoDetail(generic.DetailView):
    model = Kino

# def num(request,num):
#     print(num)
#     return render(request,'index.html')