# Generated by Django 2.2.1 on 2019-06-02 23:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torre', '0004_auto_20190602_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='torre',
            name='numero_pisos',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
