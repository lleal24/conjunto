# Generated by Django 2.2.1 on 2019-06-02 23:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torre', '0005_auto_20190602_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='torre',
            name='numero_pisos',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9)]),
        ),
    ]
