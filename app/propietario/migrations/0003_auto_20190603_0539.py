# Generated by Django 2.2.1 on 2019-06-03 05:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propietario', '0002_auto_20190603_0536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propietario',
            name='celular',
            field=models.TextField(validators=[django.core.validators.RegexValidator('([0-9]){10}', 'campo numerico de 10 digitos')]),
        ),
        migrations.AlterField(
            model_name='propietario',
            name='telefono1',
            field=models.TextField(validators=[django.core.validators.RegexValidator('([0-9]){7}', 'campo numerico de 7 digitos')]),
        ),
        migrations.AlterField(
            model_name='propietario',
            name='telefono2',
            field=models.TextField(blank=True, validators=[django.core.validators.RegexValidator('([0-9]){7}', 'campo numerico de 7 digitos')]),
        ),
    ]
