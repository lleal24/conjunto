# Generated by Django 2.2.1 on 2019-06-03 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salon',
            name='estado',
            field=models.CharField(choices=[('D', 'Disponible'), ('N', 'No disponible')], max_length=1),
        ),
    ]
