# Generated by Django 2.2.1 on 2019-06-03 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('propietario', '0001_initial'),
        ('apartamento', '0002_auto_20190602_2358'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartamento',
            name='propietario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='propietario.Propietario'),
        ),
    ]
