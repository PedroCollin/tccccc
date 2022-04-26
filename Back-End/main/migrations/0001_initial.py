# Generated by Django 3.2.9 on 2022-03-31 11:24

import cpf_field.models
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('rg', models.CharField(max_length=10)),
                ('cpf', cpf_field.models.CPFField(blank=True, max_length=14, verbose_name='Cpf')),
            ],
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=255)),
                ('descricao', models.TextField(blank=True)),
                ('data_inicio', models.DateField(default=datetime.datetime(2022, 3, 31, 8, 24, 51, 43863))),
                ('data_termino', models.DateField(default=datetime.datetime(2022, 3, 31, 8, 24, 51, 43863))),
            ],
        ),
        migrations.CreateModel(
            name='Dinamica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('descricao', models.TextField(blank=True)),
                ('duracao', models.TimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='StatusEntrevista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='StatusVaga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vaga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidadeVaga', models.IntegerField(blank=True)),
                ('dataAbertura', models.DateField()),
                ('dataFechamento', models.DateField()),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.curso')),
                ('statusVaga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.statusvaga')),
            ],
        ),
        migrations.CreateModel(
            name='VagaDinamica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, max_length=50)),
                ('dinamica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.dinamica')),
                ('vaga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.vaga')),
            ],
        ),
        migrations.CreateModel(
            name='RespostaDinamica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_criterios', jsonfield.fields.JSONField(blank=True, default=dict)),
                ('nota', models.IntegerField(blank=True)),
                ('observacao', models.TextField(blank=True)),
                ('candidato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.candidato')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vagaDinamica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.vagadinamica')),
            ],
        ),
        migrations.CreateModel(
            name='Entrevista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('observacao', models.TextField()),
                ('candidato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.candidato')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.statusentrevista')),
            ],
        ),
        migrations.AddField(
            model_name='candidato',
            name='cidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.cidade'),
        ),
        migrations.AddField(
            model_name='candidato',
            name='vaga',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.vaga'),
        ),
        migrations.CreateModel(
            name='AvaliacaoDinamica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criterio', models.CharField(blank=True, max_length=50)),
                ('peso', models.IntegerField(blank=True)),
                ('dinamica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.dinamica')),
            ],
        ),
        migrations.CreateModel(
            name='AprovacaoDinamica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.candidato')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]