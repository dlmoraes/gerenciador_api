# coding = utf-8

from django.contrib import admin

from .models import Caderno, Etiqueta, Nota

admin.register(Caderno)
class CadernoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'usu_origem', 'usu_mod', 'dta_mod',)

admin.register(Etiqueta)
class EtiquetaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'usu_origem',)

admin.register(Nota)
class NotaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'etiquetas', 'usu_origem', 'usu_mod',)