# Generated by Django 2.1.2 on 2018-11-05 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fichasnegociacao', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ficha',
            name='pddperdas_cnr',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ficha',
            name='responsavel',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='ficha',
            name='unidade_leitura',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
