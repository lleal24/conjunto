# Generated by Django 2.2.1 on 2019-06-03 22:49

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('conjunto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cartelera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.TextField(max_length=45, validators=[django.core.validators.RegexValidator('([A-Z])\\w+', 'campo solo admite letras')])),
                ('contenido', models.TextField(max_length=254, validators=[django.core.validators.RegexValidator('([A-Z])\\w+', 'campo solo admite letras')])),
                ('fecha_inicio', models.DateField(default=datetime.datetime.now)),
                ('fecha_fin', models.DateField(default=datetime.datetime.now)),
                ('conjunto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='conjunto.Conjunto')),
            ],
        ),
    ]
