# coding - utf-8

from django.contrib import admin

from .models import Perfil

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    pass