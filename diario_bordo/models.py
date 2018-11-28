# coding = utf-8

from dateutil.parser import parse
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from .lists import SITUACOES_CHOICES
from core.models import ControleData
from core.utils import formatoDeHoras


class Diario(ControleData):
    usu_origem = models.ForeignKey(User, on_delete=models.CASCADE, related_name='diario_criado')
    usu_mod = models.ForeignKey(User, on_delete=models.CASCADE, related_name='diario_modificado', null=True, blank=True)
    dta_ocor = models.DateTimeField('data da ocorrência')
    dta_concl = models.DateTimeField('data de conclusão', null=True, blank=True)
    situacao = models.CharField('situação', max_length=2, choices=SITUACOES_CHOICES, default='AT')
    geracao_compl = models.BooleanField(default=False)
    hr_ocioso = models.TimeField('Tempo Ocioso', null=True, blank=True)
    motivo_causa = models.TextField('Causa do Erro')
    motivo_reducao = models.TextField('Motivos Reduções', null=True, blank=True)

    class Meta:
        verbose_name = 'Diário'
        verbose_name_plural = 'Diários'