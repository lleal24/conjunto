# Generated by Django 2.2.1 on 2019-06-03 18:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torre', '0007_auto_20190603_0604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='torre',
            name='nombre_torre',
            field=models.TextField(max_length=50, validators=[django.core.validators.RegexValidator('([A-Z])\\w+', 'campo solo admite letras')]),
        ),
    ]
