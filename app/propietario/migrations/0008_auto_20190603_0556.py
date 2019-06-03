# Generated by Django 2.2.1 on 2019-06-03 05:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propietario', '0007_auto_20190603_0553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propietario',
            name='celular',
            field=models.TextField(max_length=10, validators=[django.core.validators.RegexValidator('([0-9]){10}', 'campo numerico de 10 digitos')]),
        ),
        migrations.AlterField(
            model_name='propietario',
            name='correo',
            field=models.EmailField(max_length=45),
        ),
        migrations.AlterField(
            model_name='propietario',
            name='telefono1',
            field=models.TextField(max_length=7, validators=[django.core.validators.RegexValidator('([0-9]){7}', 'campo numerico de 7 digitos')]),
        ),
        migrations.AlterField(
            model_name='propietario',
            name='telefono2',
            field=models.TextField(blank=True, max_length=7, validators=[django.core.validators.RegexValidator('([0-9]){7}', 'campo numerico de 7 digitos')]),
        ),
    ]