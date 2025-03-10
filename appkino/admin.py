from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Artist)
admin.site.register(Director)
admin.site.register(Genre)
admin.site.register(Country)

class adminProfile(admin.ModelAdmin):
    list_display = ('user','podpiska','balance')
admin.site.register(Profile, adminProfile)

class adminPodpiska(admin.ModelAdmin):
    list_display = ('title','price')

admin.site.register(Podpiska, adminPodpiska)

class adminKino(admin.ModelAdmin):
    list_display = ('title','director','year','podpiska')
    fieldsets = (
        ('О фильме',{'fields':('title','info','year','country','genre')}),
        ('Люди',{'fields':('director','artist')}),
        ('Для сайта',{'fields':('podpiska','rating','poster','trailer')}),
    )

admin.site.register(Kino, adminKino)

class adminOtziv(admin.ModelAdmin):
    list_display = ('user','film')
admin.site.register(Otziv, adminOtziv)

