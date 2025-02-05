"""
URL configuration for django42Kino project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from tkinter.font import names

from django.contrib import admin
from django.urls import path
from appkino import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('kino/', views.kinoList.as_view() , name = 'allkino'),
    path('artist/', views.artistList.as_view() , name = 'allartists'),
    path('kino/<str:title>/<int:pk>/', views.kinoDetail.as_view() , name = 'oneKino'),
    # path('kino/<str:num>', views.num , name = 'oneKino'),
]
