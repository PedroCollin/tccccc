# Generated by Django 3.2.9 on 2022-03-31 11:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20220331_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='data_inicio',
            field=models.DateField(default=datetime.datetime(2022, 3, 31, 8, 28, 28, 211103)),
        ),
        migrations.AlterField(
            model_name='curso',
            name='data_termino',
            field=models.DateField(default=datetime.datetime(2022, 3, 31, 8, 28, 28, 211103)),
        ),
        migrations.AlterField(
            model_name='respostadinamica',
            name='nota',
            field=models.IntegerField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='respostadinamica',
            name='observacao',
            field=models.TextField(blank=True, default=None),
        ),
    ]
