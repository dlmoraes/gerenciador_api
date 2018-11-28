# coding = utf-8

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from core.models import ControleData


class Perfil(ControleData):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil_usuario')
    avatar = models.ImageField(upload_to='imagens/avatar', default='imagens/avatar/no_imagem.gif')

    class Meta:
        verbose_name_plural = 'Perfis'

    def __str__(self):
        return self.usuario.username


@receiver(post_save, sender=User)
def criar_perfil_de_usuario(sender, **kwargs):
    if kwargs.get('created', False):
        Perfil.objects.get_or_create(usuario=kwargs.get('instance'))