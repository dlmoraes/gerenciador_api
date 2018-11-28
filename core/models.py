# coding = utf-8

from django.db import models

class ControleData(models.Model):
    dta_origem = models.DateField('data origem', auto_now_add=True, auto_now=False)
    dta_mod = models.DateField('data modificação', auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True