# Generated by Django 2.2.1 on 2019-06-03 04:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0003_auto_20190603_0437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='NIT',
            field=models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(11111111), django.core.validators.MaxValueValidator(99999999)]),
        ),
    ]
