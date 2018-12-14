# coding = utf-8
from django.contrib.auth.models import User
from django.db import models

from core.models import ControleData

class Caderno(ControleData):
    nome = models.CharField(max_length=100)
    usu_origem = models.ForeignKey(User, on_delete=models.CASCADE, related_name='caderno_criado', verbose_name='Criado Por')
    usu_mod = models.ForeignKey(User, on_delete=models.CASCADE, related_name='caderno_modificado', null=True, blank=True, verbose_name='Modificado Por')
    favorito = models.BooleanField(default=False)

    class Meta:
        unique_together = ('nome', 'usu_origem')

class Etiqueta(ControleData):
    nome = models.CharField(max_length=100)
    usu_origem = models.ForeignKey(User, on_delete=models.CASCADE, related_name='etiqueta_criado', verbose_name='Criado Por')

    class Meta:
        unique_together = ('nome', 'usu_origem')

class Nota(ControleData):
    titulo = models.CharField(max_length=100, null=True, blank=True)
    descricao = models.TextField('descrição', null=True, blank=True)
    etiquetas = models.ManyToManyField(Etiqueta, null=True, blank=True)
    usu_origem = models.ForeignKey(User, on_delete=models.CASCADE, related_name='nota_criado', verbose_name='Criado Por')
    usu_mod = models.ForeignKey(User, on_delete=models.CASCADE, related_name='nota_modificado', null=True, blank=True, verbose_name='Modificado Por')