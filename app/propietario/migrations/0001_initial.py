# Generated by Django 2.2.1 on 2019-06-03 00:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Propietario',
            fields=[
                ('numero_identificacion', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99999999999)])),
                ('nombres', models.CharField(max_length=45)),
                ('apellidos', models.CharField(max_length=45)),
                ('telefono1', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9999999)])),
                ('telefono2', models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9999999)])),
                ('celular', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9999999999)])),
                ('correo', models.EmailField(max_length=70)),
            ],
        ),
    ]