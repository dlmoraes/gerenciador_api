# coding = utf-8

from django.contrib import admin

from .models import Diario

@admin.register(Diario)
class DiarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'dta_ocor', 'dta_concl', 'situacao', 'geracao_compl', 'hr_ocioso',)