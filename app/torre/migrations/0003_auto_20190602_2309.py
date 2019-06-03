# Generated by Django 2.2.1 on 2019-06-02 23:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torre', '0002_auto_20190602_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='torre',
            name='numero_pisos',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(9), django.core.validators.MinValueValidator(1)]),
        ),
    ]