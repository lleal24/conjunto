# Generated by Django 2.2.1 on 2019-06-03 04:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0002_auto_20190603_0435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='NIT',
            field=models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(1111111111111), django.core.validators.MaxValueValidator(9999999999999)]),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='celular',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1111111111), django.core.validators.MaxValueValidator(9999999999)]),
        ),
    ]
