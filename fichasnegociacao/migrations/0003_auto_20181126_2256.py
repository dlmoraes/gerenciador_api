# Generated by Django 2.1.3 on 2018-11-27 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fichasnegociacao', '0002_auto_20181105_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ficha',
            name='e_baixarenda',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]
