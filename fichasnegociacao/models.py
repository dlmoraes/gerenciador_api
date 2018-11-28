# -*- encoding: utf-8 -*-
# coding=utf-8

from django.db import models

models.options.DEFAULT_NAMES = models.options.DEFAULT_NAMES + ('database', )

class Ficha(models.Model):
    nome = models.CharField(max_length=150, null=True, blank=True)
    endereco = models.CharField('Endereço', max_length=250, null=True, blank=True)
    instalacao = models.CharField('Instalação', max_length=15, null=True, blank=True)
    status_inst = models.CharField('Status da Instalação', max_length=2, null=True, blank=True)
    bairro = models.CharField(max_length=150, null=True, blank=True)
    complemento = models.CharField(max_length=200, null=True, blank=True)
    zona = models.CharField(max_length=2, null=True, blank=True)
    classe = models.CharField(max_length=2, null=True, blank=True)
    cc = models.CharField(max_length=25, null=True, blank=True)
    email = models.EmailField(max_length=150, null=True, blank=True)
    telefone = models.CharField(max_length=50, null=True, blank=True)
    localidade = models.CharField(max_length=60, null=True, blank=True)
    etapa = models.CharField(max_length=2, null=True, blank=True)
    livro = models.CharField(max_length=15, null=True, blank=True)
    sequencia = models.CharField(max_length=5, null=True, blank=True)
    referencia = models.CharField(max_length=250, null=True, blank=True)
    faturas = models.IntegerField(null=True)
    debito = models.FloatField(null=True, blank=True)
    cnr = models.FloatField(null=True, blank=True)
    total = models.FloatField(null=True, blank=True)
    pddperdas = models.FloatField(null=True, blank=True)
    lf = models.FloatField(null=True, blank=True)
    medidor = models.CharField(max_length=50, null=True, blank=True)
    bloq = models.FloatField(null=True, blank=True)
    e_baixarenda = models.CharField(max_length=1, null=True, blank=True)
    pddperdas_cnr = models.FloatField(blank=True, null=True)
    responsavel = models.CharField(blank=True, max_length=40, null=True)
    unidade_leitura = models.CharField(blank=True, max_length=40, null=True)

    class Meta:
        verbose_name = 'Ficha de Negociação'
        verbose_name_plural = 'Fichas de Negociação'
        database = 'fichas'

    def __str__(self):
        return self.instalacao