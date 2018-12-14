# Generated by Django 2.1.3 on 2018-11-16 19:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Diario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dta_origem', models.DateField(auto_now_add=True, verbose_name='data origem')),
                ('dta_mod', models.DateField(auto_now=True, verbose_name='data modificação')),
                ('dta_ocor', models.DateTimeField(verbose_name='data da ocorrência')),
                ('dta_concl', models.DateTimeField(blank=True, null=True, verbose_name='data de conclusão')),
                ('situacao', models.CharField(choices=[('AT', 'Ativo'), ('CO', 'Concluído')], default='AT', max_length=2, verbose_name='situação')),
                ('geracao_compl', models.BooleanField(default=False)),
                ('hr_ocioso', models.TimeField(blank=True, null=True, verbose_name='Tempo Ocioso')),
                ('motivo_causa', models.TextField(verbose_name='Causa do Erro')),
                ('motivo_reducao', models.TextField(blank=True, null=True, verbose_name='Motivos Reduções')),
                ('usu_mod', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='diario_modificado', to=settings.AUTH_USER_MODEL)),
                ('usu_origem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diario_criado', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Diário',
                'verbose_name_plural': 'Diários',
            },
        ),
    ]
