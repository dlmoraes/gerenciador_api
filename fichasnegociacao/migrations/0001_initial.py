# Generated by Django 2.1.2 on 2018-10-11 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ficha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=150, null=True)),
                ('endereco', models.CharField(blank=True, max_length=250, null=True, verbose_name='Endereço')),
                ('instalacao', models.CharField(blank=True, max_length=15, null=True, verbose_name='Instalação')),
                ('status_inst', models.CharField(blank=True, max_length=2, null=True, verbose_name='Status da Instalação')),
                ('bairro', models.CharField(blank=True, max_length=150, null=True)),
                ('complemento', models.CharField(blank=True, max_length=200, null=True)),
                ('zona', models.CharField(blank=True, max_length=2, null=True)),
                ('classe', models.CharField(blank=True, max_length=2, null=True)),
                ('cc', models.CharField(blank=True, max_length=25, null=True)),
                ('email', models.EmailField(blank=True, max_length=150, null=True)),
                ('telefone', models.CharField(blank=True, max_length=50, null=True)),
                ('localidade', models.CharField(blank=True, max_length=60, null=True)),
                ('etapa', models.CharField(blank=True, max_length=2, null=True)),
                ('livro', models.CharField(blank=True, max_length=15, null=True)),
                ('sequencia', models.CharField(blank=True, max_length=5, null=True)),
                ('referencia', models.CharField(blank=True, max_length=250, null=True)),
                ('faturas', models.IntegerField(null=True)),
                ('debito', models.FloatField(blank=True, null=True)),
                ('cnr', models.FloatField(blank=True, null=True)),
                ('total', models.FloatField(blank=True, null=True)),
                ('pddperdas', models.FloatField(blank=True, null=True)),
                ('lf', models.FloatField(blank=True, null=True)),
                ('medidor', models.CharField(blank=True, max_length=50, null=True)),
                ('bloq', models.FloatField(blank=True, null=True)),
                ('e_baixarenda', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Ficha de Negociação',
                'verbose_name_plural': 'Fichas de Negociação',
            },
        ),
    ]
