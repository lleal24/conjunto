# Generated by Django 2.2.1 on 2019-06-02 23:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torre', '0003_auto_20190602_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='torre',
            name='numero_pisos',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
