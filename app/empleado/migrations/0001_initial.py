# Generated by Django 2.2.1 on 2019-06-03 18:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresa', '0010_auto_20190603_0528'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('numero_identificacion', models.TextField(max_length=11, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('([0-9]){8,11}', 'campo numerico de almenos 8 digitos max 11')])),
                ('nombres', models.TextField(max_length=45, validators=[django.core.validators.RegexValidator('([A-Z])\\w+', 'campo solo admite letras')])),
                ('apellidos', models.TextField(max_length=45, validators=[django.core.validators.RegexValidator('([A-Z])\\w+', 'campo solo admite letras')])),
                ('direccion', models.TextField(max_length=45)),
                ('telefono1', models.TextField(max_length=7, validators=[django.core.validators.RegexValidator('([0-9]){7}', 'campo numerico de 7 digitos')])),
                ('telefono2', models.TextField(blank=True, max_length=7, validators=[django.core.validators.RegexValidator('([0-9]){7}', 'campo numerico de 7 digitos')])),
                ('celular', models.TextField(max_length=10, validators=[django.core.validators.RegexValidator('([0-9]){10}', 'campo numerico de 10 digitos')])),
                ('correo', models.EmailField(max_length=45)),
                ('estado', models.CharField(choices=[('A', 'Activo'), ('N', 'No activo')], max_length=1)),
                ('empresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='empresa.Empresa')),
            ],
        ),
    ]
